# Tem como finalidade ler os parametros passados pela linha de comando


import argparse
import os
import sys

class ParamReader:
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Ler parâmetros da linha de comando")
        self.parser.add_argument('-e', '-ext', nargs='*', choices=['pdf', 'docx', 'odt'], default=['pdf', 'docx', 'odt'], help="Tipos de extensão a serem gerados")
        self.parser.add_argument('-t', choices=['hpfa', 'kyc', 'rules'], default='kyc', help="Template a ser utilizado")
        self.parser.add_argument('-v', required=True, help="Diretório onde se encontra o arquivo variable.yaml")

    def parse_args(self):
        return self.parser.parse_args()
    
    def get_path_variavel(self, contrato_basedir, contrato_dir):
        variavel_path = os.path.join(contrato_dir, 'variable.yaml')
        if os.path.isdir(contrato_dir) and os.path.isfile(variavel_path):
            return variavel_path
        else:
            variavel_path = os.path.join(contrato_basedir, contrato_dir, 'variable.yaml')
            if os.path.isfile(variavel_path):
                return variavel_path
            else:
                print("Erro: variavel.yaml não foi localizada em ", variavel_path)
                sys.exit(1)


# if __name__ == "__main__":
#     param_reader = ParamReader()
#     args = param_reader.parse_args()
#     print(f"Extensões: {args.e}")
#     print(f"Template: {args.t}")
#     print(f"Diretório do arquivo variavel.yaml: {args.v}")