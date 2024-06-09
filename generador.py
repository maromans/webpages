import os
import subprocess

# Directorio que contiene los archivos Markdown
markdown_directory = '/Users/marcelomansilla/proyectos/webpages/bases'
# Directorio donde se guardarán las páginas HTML generadas
output_directory = '/Users/marcelomansilla/proyectos/webpages/salida'

# Crear el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Lista para almacenar los enlaces al índice
index_links = []

# Información del Dr. Mansilla Marcelo
autor_info = 'Dr. Mansilla Marcelo<br>maromansios@gmail.com'

# Procesar cada archivo Markdown en el directorio
for filename in os.listdir(markdown_directory):
    if filename.endswith('.md'):
        # Ruta completa del archivo Markdown
        filepath = os.path.join(markdown_directory, filename)

        # Nombre del archivo HTML de salida
        html_filename = filename.replace('.md', '.html')
        output_filepath = os.path.join(output_directory, html_filename)

        # Convertir Markdown a HTML usando pandoc
        subprocess.run(['pandoc', '-s', filepath, '-o', output_filepath])

        # Añadir información del autor al final del archivo HTML
        with open(output_filepath, 'a', encoding='utf-8') as html_file:
            html_file.write(f'<footer>{autor_info}</footer>')

        # Añadir enlace al índice
        index_links.append(f'<li><a href="{html_filename}">{filename.replace(".md", "")}</a></li>')

# Generar el archivo index.html
index_content = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice</title>
</head>
<body>
    <h1>Índice</h1>
    <ul>
'''
index_content += '\n'.join(index_links)
index_content += '''
    </ul>
</body>
</html>
'''

index_filepath = os.path.join(output_directory, 'index.html')
with open(index_filepath, 'w', encoding='utf-8') as index_file:
    index_file.write(index_content)

print('Generación de páginas HTML y índice completada.')
