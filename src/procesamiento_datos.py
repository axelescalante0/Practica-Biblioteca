# Funciones para procesar datos
"""from lectura import leer_csv, validar_calidad
from conversor import convertir_isbn, eliminar_filas_sin_isbn"""
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath('C:/Users/Axel/Desktop/Prueba-estructura'))

from src import lectura, conversor


libros_t = lectura.leer_csv('data/crudos/total_koha.csv')

lectura.validar_calidad(libros_t) # Verificar calidad de los datos


libros_t2 = libros_t[['title','author','isbn']]
lectura.validar_calidad(libros_t2) # Verificar calidad de los datos

libros_t2 = libros_t2.drop_duplicates() # Eliminar duplicados

# Separar los ISBNs si están separados por espacio o "|", quedándonos con el primero
libros_t2['isbn'] = libros_t2['isbn'].str.split('|').str[0].str.strip()

new_libros = conversor.convertir_isbn(libros_t2,'isbn') # Convertir los ISBNs a 13 dígitos


print(new_libros.info()) #Libros con los ISBN convertidos a 13 digitos

new_libros = conversor.eliminar_filas_sin_isbn(new_libros) # Eliminar filas sin ISBN pero con título y autor presentes en otras filas

a = new_libros[new_libros['isbn'].isna()]
print(a.info())

# Leer el archivo junto.csv
junto_df = pd.read_csv('data/procesados/junto.csv') # Archivo con los datos concatenados para buscar coincidencias, si lo hay eliminarlos

# Filtrar el DataFrame new_libros para encontrar coincidencias
new_libros = new_libros[~new_libros['title'].isin(junto_df['title'])]
#new_libros.to_csv('data/procesados/libros_total_koha.csv', index=False) # Guardar el DataFrame resultante de total koha en un archivo CSV