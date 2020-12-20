import pytesseract

def chay(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text=pytesseract.image_to_string(img)
    return text
