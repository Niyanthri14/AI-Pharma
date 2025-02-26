import streamlit as st
from google.cloud import vision
import io
import os

# Set page title and icon
st.set_page_config(page_title="Upload & Analyze Prescription", page_icon="📄")

st.title("📄 Upload & Analyze Prescription")
st.markdown("### Upload a prescription image to extract medicine names.", unsafe_allow_html=True)

# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/service_accounts.json"

# Initialize Google Vision API Client
client = vision.ImageAnnotatorClient()

# File Upload Section
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Prescription", use_column_width=True)
    
    # Convert image to byte stream
    image_content = uploaded_file.read()
    image = vision.Image(content=image_content)
    
    # Perform text detection
    response = client.text_detection(image=image)
    
    # Handle cases where no text is found
    if response.text_annotations:
        extracted_text = response.text_annotations[0].description
        st.markdown("### 📝 Extracted Text:")
        st.text_area("Extracted Text:", extracted_text, height=200)
    else:
        st.warning("⚠️ No text detected. Please upload a clearer image.")

    st.success("✅ Analysis Complete!")
