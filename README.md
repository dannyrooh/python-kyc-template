# python-kyc-template

Projeto recebe um arquivo .odt como template, um arquivo .txt com parametro para substituir as variaveis no template, e gera um novo arquivo .odt, cria um versão .docx e gera um versão em .pdt

## Requesitos

Instalar a biblioteca [pandoc](https://pandoc.org/installing.html) https://pandoc.org/installing.html

```shell
choco install pandoc
```

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

## Output

When you run the application, it will display the following message in the console:

```shell
Arquivo processado
```

## License

This project is licensed under the MIT License.