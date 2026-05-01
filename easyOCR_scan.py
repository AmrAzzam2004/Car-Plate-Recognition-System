import easyocr  

def easyOCR_scan(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    return result