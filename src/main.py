import os
from datetime import datetime
from shutil import copyfile

# Define the source and destination paths
source_path = os.path.join(os.path.dirname(__file__), 'template', 'kyc2025.odt')
destination_dir = os.path.join(os.path.dirname(__file__), 'kyc')
os.makedirs(destination_dir, exist_ok=True)

# Generate the destination file name with the current date and time
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
destination_path = os.path.join(destination_dir, f'kyc_{current_time}.odt')

# Copy the file
copyfile(source_path, destination_path)

print("Arquivo processado")