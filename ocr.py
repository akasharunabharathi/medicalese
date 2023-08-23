import pytesseract
from PIL import Image


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'usr/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def image_report(file_name: str):
    """
    Takes an image as input, and returns text from the image as a string.
    """
    image = Image.open(file_name)
    result = pytesseract.image_to_string(image)

    return result
