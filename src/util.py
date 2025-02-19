import os
from shutil import copyfile
from datetime import datetime
import yaml
from odf.opendocument import load
from odf.text import P
from dotenv import load_dotenv
from odf.draw import Frame, Image
from odf.style import Style, GraphicProperties
import subprocess


load_dotenv()

# Constants
LIBREOFFICE_PATH = os.getenv('LIBREOFFICE_PATH')
TEMPLATE_KYC = os.getenv('TEMPLATE_KYC')
TEMPLATE_HPFA = os.getenv('TEMPLATE_HPFA')
TEMPLATE_RULES = os.getenv('TEMPLATE_RULES')

def get_contrato_basedir():
    return os.getenv('SOURCE_KYC')


def get_template_path(template):
    if template == 'hpfa':
        return TEMPLATE_HPFA
    elif template == 'kyc':
        return TEMPLATE_KYC
    elif template == 'rules':
        return TEMPLATE_RULES
    else:
        raise ValueError("Template inválido")
    




def save_file(file_template,path_file_output, file_destiny):
    # Define the destination directory
    # destination_dir = os.path.join(os.path.dirname(__file__), 'kyc')
    print(file_destiny)
    os.makedirs(path_file_output, exist_ok=True)

    # # Generate the destination file name with the current date and time
    # current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    # destination_path = os.path.join(destination_dir, f'{prefix}_{current_time}.odt')
    destination_path = os.path.join(path_file_output, file_destiny)

    # destination_path = os.path.join(file_name_save, '.odt')

    # Copy the file
    copyfile(file_template, destination_path)
    print("Arquivo template copiado para: ", destination_path) 

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

def get_variable_value(data_values, key_search):
    for key, value in data_values:
        if key == key_search.upper():
            return value
    return ''


def replace_text_in_odt(file_path, replacements):
    # Load the ODT file
    doc = load(file_path)
    # print('lido arquivo', file_path)
    
    def replace_in_node(node):
        if node.nodeType == node.TEXT_NODE:  # Verifica se é um nó de texto válido
            for key, value in replacements:
                value_str = str(value)  # Converte o valor para string
                if key in node.data:
                    node.data = node.data.replace(key, value_str)
        elif node.nodeType == node.ELEMENT_NODE:  # Verifica elementos internos
            for child in node.childNodes:
                replace_in_node(child)
    
    # Percorrer todos os parágrafos do documento
    for paragraph in doc.getElementsByType(P):
        for node in paragraph.childNodes:  # Percorre todos os elementos dentro do parágrafo
            replace_in_node(node)

    doc.save(file_path)

def convert_odt_to_docx(file_path, output_dir):
    
    print('convert_odt_to_docx: ',file_path)
    # Define the destination path for the DOCX file
    destination_path = file_path.replace('.odt', '.docx')

    # Run the LibreOffice command to convert the file
    subprocess.run([LIBREOFFICE_PATH, "--headless", "--convert-to", "docx", file_path, "--outdir", output_dir], check=True)

    print(f"Arquivo convertido para .docx: {destination_path}")

def convert_odt_to_pdf(file_path):
    # Define the destination path for the PDF file
    destination_path = file_path.replace('.odt', '.pdf')

    # Run the LibreOffice command to convert the file
    subprocess.run([LIBREOFFICE_PATH, "--headless", "--convert-to", "pdf", file_path, "--outdir", os.path.dirname(file_path)], check=True)

    print(f"Arquivo convertido para .pdf: {destination_path}")