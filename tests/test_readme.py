import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"


class TestReadme(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme_text = README_PATH.read_text(encoding="utf-8")

    def test_readme_exists(self):
        self.assertTrue(README_PATH.exists(), "README.md should exist at the repository root")

    def test_local_markdown_links_point_to_existing_files(self):
        # Capture markdown links like: [text](target)
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", self.readme_text)

        local_links = [
            link
            for link in links
            if not link.startswith(("http://", "https://", "mailto:"))
        ]

        missing = []
        for link in local_links:
            normalized = link.strip()
            if normalized.startswith("./"):
                normalized = normalized[2:]
            target = REPO_ROOT / normalized
            if not target.exists():
                missing.append(link)

        self.assertEqual(
            missing,
            [],
            f"The following local links in README.md are broken: {missing}",
        )

    def test_embedded_images_exist(self):
        # Capture image links like: ![alt](path)
        image_links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", self.readme_text)

        missing_images = []
        for image_path in image_links:
            normalized = image_path.strip()
            if normalized.startswith("./"):
                normalized = normalized[2:]
            target = REPO_ROOT / normalized
            if not target.exists():
                missing_images.append(image_path)

        self.assertEqual(
            missing_images,
            [],
            f"The following image paths in README.md are missing: {missing_images}",
        )


if __name__ == "__main__":
    unittest.main()
