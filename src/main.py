import os
from datetime import datetime

from util import save_file, read_yaml_variavel, replace_text_in_odt, convert_odt_to_docx, convert_odt_to_pdf, get_contrato_basedir, get_template_path, get_variable_value

from param import ParamReader

if __name__ == "__main__":
    param_reader = ParamReader()
    args = param_reader.parse_args()

    path_file_variable = param_reader.get_path_variavel(get_contrato_basedir(), args.v)
    
    print(f"Extensões: {args.e}")
    print(f"Template: {args.t}") 

# Define the source paths
# source_path = os.path.join(os.path.dirname(__file__), 'template', 'template.odt')

# Template
file_template = get_template_path(args.t)

print(file_template)

prefix = args.t


# Call the function to read the YAML file and print keys with values
yaml_data = read_yaml_variavel(path_file_variable  )

file_name_save = (args.t).upper() + '-' + str(get_variable_value(yaml_data, '#FNAME#')) + '.odt'

print(file_name_save)

path_file_output =  os.path.join(get_contrato_basedir(), args.v, 'out', datetime.now().strftime('%Y%m%d_%H%M%S'))

print(file_template)
print(path_file_output)

# Call the function to save the file
path_saved = save_file(file_template, path_file_output, file_name_save)

# print('savedfile: ', path_saved)

# print(yaml_data)

# Call the function to replace text in the ODT file
# replace_text_in_odt(path_saved, replacements)
replace_text_in_odt(path_saved, yaml_data)

if 'pdf' in args.e:
    convert_odt_to_pdf(path_saved)

if 'docx' in args.e:
    convert_odt_to_docx(path_saved,path_file_output)

# if 'odt' not in args.e:
#     os.remove(path_saved)
    

