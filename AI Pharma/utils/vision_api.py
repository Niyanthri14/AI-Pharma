import os
from google.cloud import vision
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/service_accounts.json"

def extract_text_from_image(image_path):
    """Extracts text from a given prescription image using Google Vision API."""
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    return "No text detected."
