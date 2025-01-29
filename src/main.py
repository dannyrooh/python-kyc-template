import os
from datetime import datetime
from shutil import copyfile
import yaml

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

def read_yaml_and_print_keys(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        for section in data.values():
            if isinstance(section, dict):
                for key, value in section.items():
                       if isinstance(value, dict):
                           for k, v in value.items():
                               formatted_key = f"#{k.upper()}#"
                               print(f"{formatted_key}: {v}")
                       else:
                           formatted_key = f"#{key.upper()}#"
                           print(f"{formatted_key}: {value}")

# Define the source paths
source_path = os.path.join(os.path.dirname(__file__), 'template', 'kyc2025.odt')
yaml_path = os.path.join(os.path.dirname(__file__), 'kyc-var', 'variables.yaml')

# Call the function to save the file
save_file(source_path)

# Call the function to read the YAML file and print keys with values
read_yaml_and_print_keys(yaml_path)