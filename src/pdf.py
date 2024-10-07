import os
import pdfplumber
import re
import pandas as pd 
import sys

sys.path.append(os.path.abspath('C:/Users/Axel/Desktop/Practica-Biblioteca'))


# Directorio local donde están los archivos PDF
pdf_directory = "C:/Users/Axel/Downloads/2024"  # Cambia esto a tu ruta local

# Lista para almacenar la información extraída
data = []

# Función para extraer información de un PDF
def extraer_informacion(pdf_texto):
    # Buscar la carrera (suponiendo que empieza con 'Carrera:')
    carrera = re.search(r'Carrera:\s*(.*)', pdf_texto)
    carrera = carrera.group(1) if carrera else 'No encontrado'

    # Buscar la asignatura (suponiendo que empieza con 'Asignatura:')
    asignatura = re.search(r'Asignatura:\s*(.*)', pdf_texto)
    asignatura = asignatura.group(1) if asignatura else 'No encontrado'

    # Buscar la bibliografía principal (suponiendo que empieza con 'Bibliografía Principal:')
    bibliografia = re.search(r'Bibliografia Principal:\s*(.*?)\s*Bibliografia Complementaria:', pdf_texto, re.DOTALL)
    bibliografia = bibliografia.group(1).strip() if bibliografia else 'No encontrado' #

    return carrera, asignatura, bibliografia

# Iterar sobre los archivos PDF en la carpeta local
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, filename)
        
        # Abrir el archivo PDF y extraer el texto
        with pdfplumber.open(pdf_path) as pdf:
            pdf_text = ""
            for page in pdf.pages:
                pdf_text += page.extract_text()

            # Extraer la información de carrera, asignatura, bibliografía
            carrera, asignatura, bibliografia = extraer_informacion(pdf_text)

            # Agregar la información a la lista
            data.append([filename, carrera, asignatura, bibliografia])

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(data, columns=["Archivo", "Carrera", "Asignatura", "Bibliografía"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("informacion_catedra.xlsx", index=False)

print("Proceso completado. La información se ha guardado en 'informacion_catedra.xlsx'.")
