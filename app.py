import streamlit as st
from PIL import Image
import io

st.title("Artisan Product Submission Form")

uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])
 
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write("Filename: ", uploaded_file.name)
    # st.write(bytes_data)  # This will display the raw bytes, typically not useful for users

    # To display the image
    image = Image.open(io.BytesIO(bytes_data))
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Creating text input box

st.header("Tell us about your product")

# Input fields
product_type = st.text_input("Type of Product", placeholder="e.g., Handmade Jewelry, Pottery, Painting")
product_origin = st.text_input("Product Origin", placeholder="e.g., City, Country, Region")
product_description = st.text_area("Brief Description", placeholder="Provide a brief description of your product")

# Submit button
if st.button("Submit"):
    st.write("Thank you for your submission!")
    st.write("### Product Details")
    st.write(f"**Type of Product:** {product_type}")
    st.write(f"**Product Origin:** {product_origin}")
    st.write(f"**Description:** {product_description}")