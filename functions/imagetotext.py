import easyocr


def text_recognition(file_path): #функия перевода изображения в текст 
    reader = easyocr.Reader(['ru'])
    result = reader.readtext(file_path, detail=0)
    
    return result