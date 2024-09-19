import pandas as pd
import isbnlib

def convertir_isbn(df,columna):
    """
    Convierte los números ISBN de 10 dígitos a 13 dígitos en un DataFrame.

    Parámetros:
    -----------
    df : pandas.DataFrame
    columna : str nombre de la columna

    Returns:
    --------
    pandas.DataFrame
        DataFrame con la columna  actualizada donde los ISBN de 10
        dígitos han sido convertidos a formato de 13 dígitos.
    """
    # Verificamos si el ISBN es válido (no es nulo) y si tiene 10 dígitos
    df[columna] = df[columna].apply(lambda x: isbn_10_a_13(x) if pd.notna(x) and len(x) == 10 and x[:-1].isdigit() else x)
    return df


def isbn_10_a_13(isbn_10):
    return isbnlib.to_isbn13(isbn_10)

# Ejemplo de uso
isbn_10 = '846044757X'
isbn_13 = isbn_10_a_13(isbn_10)
print(f"ISBN-10: {isbn_10} -> ISBN-13: {isbn_13}")


import pandas as pd

def eliminar_filas_sin_isbn(df, col_titulo='title', col_autor='author', col_isbn='isbn'):
    """
    Elimina las filas que no tienen ISBN, pero solo si hay al menos una fila con el mismo título y autor que sí tiene ISBN.

    :param df: DataFrame original.
    :param col_titulo: Nombre de la columna que contiene los títulos.
    :param col_autor: Nombre de la columna que contiene los autores.
    :param col_isbn: Nombre de la columna que contiene los ISBN.
    :return: DataFrame filtrado.
    """
    # Encontrar duplicados basados en el título y el autor
    duplicados = df.duplicated(subset=[col_titulo, col_autor], keep=False)

    # Crear un DataFrame solo con duplicados
    df_duplicados = df[duplicados]

    # Agrupar por título y autor y mantener solo aquellos registros que tienen al menos un ISBN definido
    grupos_con_isbn = df_duplicados.groupby([col_titulo, col_autor]).filter(lambda x: x[col_isbn].notna().any())

    # Obtener índices de los registros con ISBN
    indices_con_isbn = grupos_con_isbn.dropna(subset=[col_isbn]).index

    # Filtrar el DataFrame original eliminando las filas duplicadas sin ISBN, pero solo si hay al menos uno con ISBN
    for indice in indices_con_isbn:
        titulo = df.loc[indice, col_titulo]
        autor = df.loc[indice, col_autor]
        # Eliminar las filas donde el título y autor coinciden pero el ISBN es NaN
        df = df.drop(df[(df[col_titulo] == titulo) & (df[col_autor] == autor) & (df[col_isbn].isna())].index)

    return df

