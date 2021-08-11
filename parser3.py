import cv2
import pytesseract
#Loading image using OpenCV
img = cv2.imread('sample_image.png')
#Converting to text
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(img)
print(text)