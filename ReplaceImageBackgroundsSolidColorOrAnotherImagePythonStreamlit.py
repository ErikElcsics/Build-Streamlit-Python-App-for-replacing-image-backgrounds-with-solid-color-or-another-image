# Importing Required Modules
from rembg import remove
from PIL import Image, ImageOps
import streamlit as st
from io import BytesIO
import numpy as np

# Title of the Streamlit app
st.title("Background Remover and Replacer")

# Initialize session state for output_image if not already present
if 'output_image' not in st.session_state:
    st.session_state.output_image = None

# File uploader allows user to add their own image
uploaded_image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

    # Open the uploaded image
    pil_image = Image.open(uploaded_image)

    # Removing the background from the given Image
    with st.spinner('Removing Background...'):
        output_image = remove(pil_image)

    # Store the output image in session state
    st.session_state.output_image = output_image

    # Display the processed image
    st.image(output_image, caption="Background Removed", use_container_width=True)

    # Provide options for background replacement
    st.subheader("Replace Background")

    # Option to replace with a solid color
    replace_with_color = st.checkbox("Replace with Solid Color")
    if replace_with_color:
        # Color picker for selecting the replacement color
        color = st.color_picker("Choose Background Color", "#ffffff")
        color_rgb = Image.new("RGB", output_image.size, color)
        # Composite the solid color background with the output image
        output_image = Image.composite(output_image, color_rgb, output_image)
        st.image(output_image, caption="Background Replaced with Color", use_container_width=True)

    # Option to replace with another image
    replace_with_image = st.checkbox("Replace with Another Image")
    if replace_with_image:
        # File uploader for the background image
        bg_image = st.file_uploader("Choose a background image", type=["jpg", "jpeg", "png"])
        if bg_image:
            bg_image = Image.open(bg_image).resize(output_image.size)
            # Composite the new background with the output image
            output_image = Image.composite(output_image, bg_image, output_image)
            st.image(output_image, caption="Background Replaced with Image", use_container_width=True)

    # Convert the output image to bytes
    img_byte_arr = BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Provide a download button for the user to save the output image
    st.download_button(
        label="Download Image with New Background",
        data=img_byte_arr,
        file_name="background_replaced.png",
        mime="image/png"
    )
