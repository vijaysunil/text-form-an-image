import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
from PIL import Image

vijay = Image.open('textquotes.png')
text = tess.image_to_string(vijay)

print(text)