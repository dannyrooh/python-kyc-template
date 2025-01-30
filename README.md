# python-kyc-template

Projeto recebe um arquivo .odt como template, um arquivo .yaml com **keys e values** para substituirem as variavéis no template. Após a substituição, serão gerados os seguintes arquivos:

   - .odt (LibreOffice)
   - .docx (Word)
   - .pdf (PDF)

As variáveis a serem criadas no corpo do arquivo de template.odt, deverão corresponder as chaves no arquivo .yaml, no arquivo .yaml as chaves estão em minusculas e no template devem estar entres os caraceres # e em maisculas.

## Issue

Features e melhorias a serem implementadas

1. Receber o arquivo de template como parâmetro
2. Receber um ou mais arquivos de variaveis como parâmetro
3. Possibilitar a escolha do diretório de destino dos arquivos gerados

## Requisitos

- Possuir o LIbreOffice instalado ou path onde está o arquivo soffice.exe

---

## Como funciona

1. Ajuste e renomeie o arquivo **./template/template.odt.example** para **./template/template.odt**
2. Ajuste e renomeie o arquivo **./variavel/variaveis.yaml.example** para **./variavel/variaveis.yaml**
3. Ajuste as constantese e renomeie o arquivo **.env-example** para **.env**
4. Execute o comando **python src/main.py**


## Getting Startedn

To run this application, follow the steps below:

1. **Clone the repository**:

   ```shell
   git clone <repository-url>
   cd iib-kyc
   ```

2. **Install dependencies**:
   If you have any dependencies listed in `requirements.txt`, install them using:
   
   ```shell
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the main script:

   ```shell
   python src/main.py
   ```


## License

This project is licensed under the MIT License.