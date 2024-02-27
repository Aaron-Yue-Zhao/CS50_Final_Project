from docx import Document
from googletrans import Translator
import os 

# def read_doc(file_path):
#     doc = Document(file_path)
#     text = ''
#     for paragraph in doc.paragraphs:
#         text += paragraph.text + '\n'
#     return text

def translate_text(text, target_language='en'):
    translator = Translator() # instance of the translator object
    translated_text = translator.translate(text, dest=target_language) # method of object to translate text
    return translated_text.text # attribute of the translated text object

# def main():
#     file_path = 'your_document.docx'
#     original_text = read_doc(file_path)
#     target_language = 'en'  
#     api_key = API_KEY
#     translated_text = translate_text(original_text, target_language, api_key)

#     print(f"Original Text:\n{original_text}\n")
#     print(f"Translated Text ({target_language}):\n{translated_text}")

# if __name__ == "__main__":
#     main()
translator = Translator(service_urls=['translate.google.com'])

print(translator.translate('안녕하세요.').text)