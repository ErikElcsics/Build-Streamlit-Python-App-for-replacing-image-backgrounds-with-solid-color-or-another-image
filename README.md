# Build-Streamlit-Python-App-for-replacing-image-backgrounds-with-solid-color-or-another-image
This Streamlit application enables users to remove the background from images and replace it with a solid color or another image.​

Features

- Background Removal: The rembg library is used to remove the background from the uploaded image.​

- Background Replacement:

	- Solid Color Replacement: If the user selects the option to replace the background with a solid color, a color picker is displayed. The chosen color is then used to create a new background, which is composited with the foreground (subject) of the image.​
	- Image Replacement: If the user opts to replace the background with another image, they can upload a background image. This image is resized to match the dimensions of the original image and composited with the foreground.​
	- Image Preview: Displays the original and processed images within the app.​
	- Download Option: After processing, the user can download the image with the new background.


Installation
Clone the Repository:

git clone [https://github.com/yourusername/background-remover-replacer.git](https://github.com/ErikElcsics/Build-Streamlit-Python-App-for-replacing-image-backgrounds-with-solid-color-or-another-image.git
)
cd background-remover-replacer

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt

Run the Application:
streamlit run ReplaceImageBackgroundsSolidColorOrAnotherImagePythonStreamlit.py

Usage:
Upload an Image: Use the file uploader to select a JPG or PNG image.​
Remove Background: The app will automatically process the image to remove its background.​

Replace Background:
1. Solid Color: Select the "Replace with Solid Color" option and choose a color.​
2. Custom Image: Select the "Replace with Another Image" option and upload a background image.​
3. Download Image: Click the "Download Image with New Background" button to save the processed image.​

Dependencies:
- rembg​
- Pillow​
- Streamlit

License
This project is licensed under the MIT License.

![image](https://github.com/user-attachments/assets/a9bd2794-f870-4636-a766-d86b94e22cf7)

![image](https://github.com/user-attachments/assets/f5fbeaca-62fd-4d34-b0bb-4f9d590a0ce3)

![image](https://github.com/user-attachments/assets/192aba5d-dc4a-42de-885f-6e4770f3e0df)

![image](https://github.com/user-attachments/assets/dd2266d3-48bf-493a-9f73-64342e68fced)

![image](https://github.com/user-attachments/assets/413b6d42-8271-42ce-b945-947876ec5754)





