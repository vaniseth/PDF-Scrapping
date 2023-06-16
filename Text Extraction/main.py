import os
import pytesseract
from pdf2image import convert_from_path

pdf_dir = './PDFs/'
output_dir = './Extracted Text/'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        images = convert_from_path(pdf_path) #conversion to image
        extracted_text = ''
        
        for image in images:
            text = pytesseract.image_to_string(image, lang='eng')
            extracted_text += text

        output_file = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        print(f'Extracted text from {filename} and saved to {output_file}')
