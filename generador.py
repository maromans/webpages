import os
import markdown

# Directorio que contiene los archivos Markdown
markdown_directory = '/Users/marcelomansilla/proyectos/webpages/bases'
# Directorio donde se guardarán las páginas HTML generadas
output_directory = '/Users/marcelomansilla/proyectos/webpages/salida'

# Crear el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Lista para almacenar los enlaces al índice
index_links = []

# Procesar cada archivo Markdown en el directorio
for filename in os.listdir(markdown_directory):
    if filename.endswith('.md'):
        # Ruta completa del archivo Markdown
        filepath = os.path.join(markdown_directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            html_content = markdown.markdown(text)

            # Nombre del archivo HTML de salida
            html_filename = filename.replace('.md', '.html')
            output_filepath = os.path.join(output_directory, html_filename)

            # Escribir el contenido HTML en el archivo de salida
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(html_content)

            # Añadir enlace al índice
            index_links.append(f'<li><a href="{html_filename}">{html_filename}</a></li>')

# Generar el archivo index.html
index_content = '<html><head><title>Índice</title></head><body>'
index_content += '<h1>Índice</h1><ul>'
index_content += '\n'.join(index_links)
index_content += '</ul></body></html>'

index_filepath = os.path.join(output_directory, 'index.html')
with open(index_filepath, 'w', encoding='utf-8') as index_file:
    index_file.write(index_content)

print('Generación de páginas HTML y índice completada.')
