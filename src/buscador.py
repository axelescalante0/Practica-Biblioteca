#modulo para buscar libros por titulo, autor o ISBN
import sys
import os

sys.path.append(os.path.abspath('C:/Users/Axel/Desktop/Practica-Biblioteca'))

import pandas as pd

csv = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_biblioteca.csv'
df = pd.read_csv(csv, delimiter=',')

def buscar_libro(df, columna, valor):
    """
    Busca un libro en la base de datos de la biblioteca.

    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con los datos de la biblioteca.
    columna : str
        Nombre de la columna por la cual se buscará el libro.
    valor : str
        Valor a buscar en la columna especificada.

    Returns:
    --------
    pandas.DataFrame
        DataFrame con los datos del libro encontrado.
    """
    #pasar a minusculas el valor de la columna
    df[columna] = df[columna].str.lower()
    #pasar a minusculas el valor a buscar
    valor = valor.lower()
    #buscar el libro donde es un string, puedo buscar por titulo completo o por una parte del titulo
    libro = df[df[columna].str.contains(valor, case=False, na=False)]
    return libro


#eje de prueba
libro = buscar_libro(df, 'title', 'edición')

print(libro.info())