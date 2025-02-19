from odf.opendocument import load, OpenDocumentText
from odf.text import P
from odf.draw import Frame, Image
from odf.style import Style, GraphicProperties

def insert_image_in_odt(file_path, tag, image_path):
    # Load the ODT file
    doc = load(file_path)
    print('lido arquivo', file_path)
    
    # Define the style for the image
    frame_style = Style(name="FrameStyle", family="graphic")
    frame_style.addElement(GraphicProperties(stroke="none", fill="none"))
    doc.styles.addElement(frame_style)
    
    def replace_in_node(node):
        if node.nodeType == node.TEXT_NODE:  # Verifica se é um nó de texto válido
            if tag in node.data:
                # Create a frame for the image
                frame = Frame(
                    name="PictureFrame",
                    width="5cm",
                    height="5cm",
                    anchortype="as-char",
                    stylename=frame_style
                )
                
                # Create the image element
                image = Image(href=image_path, type="simple", show="embed", actuate="onLoad")
                frame.addElement(image)
                
                # Replace the tag with the frame
                parent = node.parentNode
                parent.insertBefore(frame, node)
                parent.removeChild(node)
        elif node.nodeType == node.ELEMENT_NODE:  # Verifica elementos internos
            for child in node.childNodes:
                replace_in_node(child)
    
    # Percorrer todos os parágrafos do documento
    for paragraph in doc.getElementsByType(P):
        for node in paragraph.childNodes:  # Percorre todos os elementos dentro do parágrafo
            replace_in_node(node)

    doc.save(file_path)
    print(f"Imagem inserida no arquivo: {file_path}")

# Exemplo de uso
file_path = "H:\\workspace-freela\\IIB\\contratos\\out\\20250214_131506\\FOLLOW_CREATION_LTDA_1,8B_ALEXANDRITE.odt"
tag = "#IMAGE_TAG#"
image_path = "H:\\workspace-freela\\IIB\\images\\example_image.png"
insert_image_in_odt(file_path, tag, image_path)

