#Desarrollo de script para cruzar los datos de la bibilioteca con el proviemiente en la catedra.
#planiacion del script

#1. Puedo aplicar un ordenamiento rapido (quick sort) a los datos de la catedra y de la biblioteca(ordenar por ISBN). Esto para luego aplicar busqueda binaria.
#2. Aplicar busqueda binaria para buscar los datos de la catedra en la biblioteca.

#Los datos resultante son de todos los años, los de la caatedra son de primer año. ¿Como puedo filtrar los datos de la biblioteca para que solo sean de primer año?--pensasr mas adelante.

from src import ordenamiento
import pandas as pd

# titulos_autores_biblioteca.csv = contiene los titulos y autores de libros disponible en la biblioteca.
# bibliografia_programas_proce = contiene los titulos y autores de las catedras de 1re año disponibles en los programas

# Determinar el porcentaje de libros de la catedra que estan en la biblioteca

# Cargar los datos

csv_catedra = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/bibliografia_programas_proce.xlsx'
csv_biblioteca = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/titulos_autores_biblioteca.csv'

df_catedra = pd.read_excel(csv_catedra)
df_biblioteca = pd.read_csv(csv_biblioteca, delimiter=',')

# Normalizar títulos y autores para facilitar la comparación
df_catedra['titulo'] = df_catedra['titulo'].str.lower().str.strip()
df_catedra['autor'] = df_catedra['autor'].str.lower().str.strip()

# cambiamos los nombres de las columnas que estan en ingles a español
df_biblioteca.rename(columns={'title':'titulo', 'author':'autor'}, inplace=True)
df_biblioteca['titulo'] = df_biblioteca['titulo'].str.lower().str.strip()
df_biblioteca['autor'] = df_biblioteca['autor'].str.lower().str.strip()

# hay titulos que tienen ":" o "/" al final de la cadena, se eliminan
df_biblioteca['titulo'] = df_biblioteca['titulo'].str.replace(':', '').str.replace('/', '').str.replace('.', '')
#lo miso para la catedra
df_catedra['titulo'] = df_catedra['titulo'].str.replace(':', '').str.replace('/', '').str.replace('.', '')

# Eliminar ':' o '/' o '.' solo al final de la cadena
df_biblioteca['autor'] = df_biblioteca['autor'].str.replace(r'[:/.]+$', '', regex=True)
df_catedra['autor'] = df_catedra['autor'].str.replace(r'[:/.]+$', '', regex=True)

df_catedra = df_catedra[['autor', 'titulo']]
df_biblioteca = df_biblioteca[['autor', 'titulo']]

df_biblioteca['titulo'] = df_biblioteca['titulo'].str.lower().str.strip()
df_catedra['titulo'] = df_catedra['titulo'].str.lower().str.strip()

# Eliminar duplicados en la bibliografía (un libro contado una vez por cada título y autor)
bibliografia_unica = df_catedra.drop_duplicates( subset=['titulo', 'autor'])

# Identificar libros disponibles en la biblioteca basándose en título y autor
libros_disponibles = bibliografia_unica[bibliografia_unica['titulo'].isin(df_biblioteca['titulo']) & bibliografia_unica['autor'].isin(df_biblioteca['autor'])]

# Calcular porcentaje de disponibilidad
porcentaje_disponible = (len(libros_disponibles) / len(bibliografia_unica)) * 100

print(f'El {porcentaje_disponible:.2f}% de los libros de la bibliografía está disponible en la biblioteca.')

print(libros_disponibles)