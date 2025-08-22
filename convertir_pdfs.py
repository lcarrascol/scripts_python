# Convert pdf files in text files that are in the same folder
# Leonidas Carrasco-Letelier
# lcarrasco@inia.org.uy

import fitz  # PyMuPDF
import os

def pdf_to_txt(folder):
    """Convierte todos los archivos PDF en la carpeta a archivos de texto plano (.txt)."""
    for filename in os.listdir(folder):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(folder, txt_filename)
            with fitz.open(pdf_path) as doc:
                text = "".join(page.get_text() for page in doc)
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Convertido: {filename} → {txt_filename}")

# Ejecutar la función en la carpeta actual
pdf_to_txt(".")
