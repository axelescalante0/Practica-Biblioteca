# Funciones para procesar datos
"""from lectura import leer_csv, validar_calidad
from conversor import convertir_isbn, eliminar_filas_sin_isbn"""
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath('C:/Users/Axel/Desktop/Prueba-estructura'))

from src import lectura, conversor

# Cargar los archivos CSV
df_catedra = pd.read_csv('bibliografia_catedras.csv')  # Primer CSV
df_biblioteca = pd.read_csv('df_biblioteca.csv')  # Segundo CSV

# Normalizar títulos y autores para facilitar la comparación
df_catedra['titulo'] = df_catedra['titulo'].str.lower().str.strip()
df_catedra['autor'] = df_catedra['autor'].str.lower().str.strip()

df_biblioteca['titulo'] = df_biblioteca['titulo'].str.lower().str.strip()
df_biblioteca['autor'] = df_biblioteca['autor'].str.lower().str.strip()

# Eliminar duplicados en la bibliografía (un libro contado una vez por cada título y autor)
bibliografia_unica = df_catedra.drop_duplicates(subset=['titulo', 'autor'])

# Identificar libros disponibles en la biblioteca
libros_disponibles = bibliografia_unica[bibliografia_unica['titulo'].isin(df_biblioteca['titulo'])]

# Calcular porcentaje de disponibilidad
porcentaje_disponible = (len(libros_disponibles) / len(bibliografia_unica)) * 100

print(f'El {porcentaje_disponible:.2f}% de los libros de la bibliografía está disponible en la biblioteca.')
