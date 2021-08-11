from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C://Program Files//Tesseract-OCR//tesseract.exe"
image_path = r"sample_image.png"
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])
# pdf = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
# with open('extractedText.pdf', 'w+b') as f:
#     f.write(pdf)