#Funcion para cruzar coincidencias entre la base de datos de la biblioteca y los programas de la catedra.

def cruzar_datos(df_biblioteca, df_catedra, columna):
    """
    Cruza los datos de la biblioteca con los datos de la cátedra.

    Parámetros:
    -----------
    df_biblioteca : pandas.DataFrame
        DataFrame con los datos de la biblioteca.
    df_catedra : pandas.DataFrame
        DataFrame con los datos de la cátedra.
    columna : str
        Nombre de la columna por la cual se cruzarán los datos.

    Returns:
    --------
    pandas.DataFrame
        DataFrame con los datos cruzados.
    """
    # Ordenar ambos DataFrames por la columna especificada
    df_biblioteca = df_biblioteca.sort_values(by=columna)
    df_catedra = df_catedra.sort_values(by=columna)

    # Cruce de los datos
    datos_cruzados = pd.merge(df_biblioteca, df_catedra, on=columna, how='inner')

    return datos_cruzados