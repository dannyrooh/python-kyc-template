import os
from datetime import datetime
from shutil import copyfile
import yaml
from odf.opendocument import load
from odf.text import P
import subprocess

def save_file(file_path):
    # Define the destination directory
    destination_dir = os.path.join(os.path.dirname(__file__), 'kyc')
    os.makedirs(destination_dir, exist_ok=True)

    # Generate the destination file name with the current date and time
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    destination_path = os.path.join(destination_dir, f'kyc_{current_time}.odt')

    # Copy the file
    copyfile(file_path, destination_path)
    print("Arquivo processado")

    return destination_path

def read_yaml_variavel(file_path):
    result = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        for section in data.values():
            if isinstance(section, dict):
                for key, value in section.items():
                    if value and not isinstance(value, (dict, list)):
                        formatted_key = f"#{key.upper()}#"
                        result.append((formatted_key, value))
    return result

def replace_text_in_odt(file_path, replacements):
    # Load the ODT file
    doc = load(file_path)
    
# Percorrer todos os parágrafos do documento
    for paragraph in doc.getElementsByType(P):
        for node in paragraph.childNodes:  # Percorre todos os elementos dentro do parágrafo
            if node.nodeType == node.TEXT_NODE:  # Verifica se é um nó de texto válido
                for key, value in replacements:
                    if key in node.data:
                        node.data = node.data.replace(key, value)
            elif node.nodeType == node.ELEMENT_NODE:  # Verifica elementos internos (ex.: <text:span>)
                if node.firstChild and node.firstChild.nodeType == node.TEXT_NODE:
                    for key, value in replacements:
                        if key in node.firstChild.data:
                            node.firstChild.data = node.firstChild.data.replace(key, value)

    doc.save(file_path)

def convert_odt_to_docx(file_path):
    # Define the destination path for the DOCX file
    destination_path = file_path.replace('.odt', '.docx')

    # Run the LibreOffice command to convert the file
    subprocess.run(["C:\\Program Files\\LibreOffice\\program\\soffice.exe", "--headless", "--convert-to", "docx", file_path, "--outdir", os.path.dirname(file_path)], check=True)

    print(f"Arquivo convertido para .docx: {destination_path}")

def convert_odt_to_pdf(file_path):
    # Define the destination path for the PDF file
    destination_path = file_path.replace('.odt', '.pdf')

    # Run the LibreOffice command to convert the file
    subprocess.run(["C:\\Program Files\\LibreOffice\\program\\soffice.exe", "--headless", "--convert-to", "pdf", file_path, "--outdir", os.path.dirname(file_path)], check=True)

    print(f"Arquivo convertido para .pdf: {destination_path}")


# Define the source paths
source_path = os.path.join(os.path.dirname(__file__), 'template', 'kyc2025.odt')
yaml_path = os.path.join(os.path.dirname(__file__), 'kyc-var', 'variables.yaml')

# Call the function to read the YAML file and print keys with values
yaml_data = read_yaml_variavel(yaml_path)

# Call the function to save the file
path_saved = save_file(source_path)

# Call the function to replace text in the ODT file
# replace_text_in_odt(path_saved, replacements)
replace_text_in_odt(path_saved, yaml_data)

# exporta para pdf
convert_odt_to_pdf(path_saved)

# Call the function to convert the ODT file to DOCX
convert_odt_to_docx(path_saved)
