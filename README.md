# GeminiGalaxy

## Description

Galaxy focus on creating custom templates and help you extract information through intelligent `Gemini` Models. Galaxy also helps you capture tables detected in your template.

Each galaxy model contains multiple templates. The number of fields to be extracted within a model are same. However, each template can have different fields to be extracted.

## Steps To Use Galaxy

### Step 1: 

Login to [staple.io](https://staple.io/login)

Please contact [josh\@staple.io](mailto:josh@staple.io) for creating an account.

![login.png](./docs/login.png)


### Step 2: Create Galaxy Model

Create a galaxy model.

![create_galaxy_model.png](./docs/galaxy_model/create_new_model_button.png)

A model creation page will pop up. Give your model a name. Select image type and choose if you want document translation while tagging.

![create_galaxy_model_page.png](./docs/galaxy_model/create_model_page.png)

Select the image processing preferences you want for your model. 
![create_galaxy_model_preference.png](./docs/galaxy_model/create_model_preference_page.png)


Now, since you have created a model.

Upload your document.

![upload_template.png](./docs/galaxy_model/upload_template_page.png)


Once your document is uploaded clicked on your document. And select the detection method.

`Detection Methods`: Detection methods are of two types: 

1. Positional Based: Where we use the spatial information to extract information.
2. Intelligence Based: Where we leverage Gemini 1.5-Pro to extract information.
   
![detection_method.png](./docs/galaxy_model/select_detection_method.png)

After selecting a detection method. You need to add Name of the field, ie. field to be extracted. You will also need to
tag keywords and data_area.
![keyword_mapping.png](./docs/galaxy_model/keyword_minibox_maping.png)

![mapping_data_area.png](./docs/galaxy_model/mapping_data_area.png)

Once you have tagged the keywords and data_area, If you have selected `intelligence based` extraction, you must add a description for your field. This will help Gemini understand what to extract.
![add_field_description.png](./docs/galaxy_model/add_field_description.png)

Now you must select the field `data_type` which best describes your field value.
![select_field_data_type.png](./docs/galaxy_model/select_field_data_type.png)


Once you have tagged all the fields that you want to extract, click on complete on the task bar to register your custom template.
![complete_template_mapping.png](./docs/galaxy_model/complete_template_mapping.png)


## Step3: Upload a Scan

Create a new queue

![Create_new_queue.png](./docs/scanning_area/Create_new_queue.png)

Add the details for your queue. Select your custom model that you have just created.

![queue_creation_page.png](./docs/scanning_area/queue_creation_page.png)

Add image pre-processing preferences for your documents. 

![queue_preference_page.png](./docs/scanning_area/queue_preference_page.png)

Now, upload the document that you want to scan

![upload_invoice.png](./docs/scanning_area/upload_invoice.png)

Once documents are scanned, your scanned document should look like this, with the extracted values.

![scanned_document.png](./docs/scanning_area/scanned_document.png)

Here are the values mapped in the document.

![field_value_and_their_mapping.png](./docs/scanning_area/fields_value_and_their_mapping.png)


## Contact Us

For any queries, contact [josh\@staple.io](mailto:josh@staple.io)
