import pandas as pd
import os

# Función para leer un archivo CSV
def leer_csv(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=';')
        print(f"Archivo {file_path} leído con éxito.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
        return None

# Función para validar la calidad de los datos
def validar_calidad(df):
    if df is not None:
        print(f"Validando calidad de datos del archivo...")
        
        #info
        print('Informacion de los datos')
        df.info()
        
        # Revisar valores faltantes
        missing_values = df.isnull().sum().sum()
        print(f"Valores faltantes: {missing_values}")
        
        # Revisar duplicados
        duplicates = df.duplicated().sum()
        print(f"Filas duplicadas: {duplicates}")
        
       
        
        # Aquí puedes agregar otras validaciones como el tipo de datos, etc.
    else:
        print("No se puede validar un DataFrame nulo.")