import sys
import os
import pandas as pd

sys.path.append(os.path.abspath('C:/Users/Axel/Desktop/Prueba-estructura'))


def juntar_csv(carpeta):
    archivos_csv = [f for f in os.listdir(carpeta) if f.endswith('.csv')]
    dataframes = [pd.read_csv(os.path.join(carpeta, archivo), delimiter=';') for archivo in archivos_csv]
    df_concatenado = pd.concat(dataframes, ignore_index=True)
    return df_concatenado

def guardar_csv(df, ruta_salida):
    df.to_csv(ruta_salida, index=False)

if __name__ == "__main__":
    carpeta_csv = 'C:/Users/Axel/Desktop/Prueba-estructura/data/crudos/ultimos listados para filtrar el original'
    archivo_salida = 'C:/Users/Axel/Desktop/Prueba-estructura/data/procesados/junto.csv'
    
    df_concatenado = juntar_csv(carpeta_csv)
    guardar_csv(df_concatenado, archivo_salida)
    print(f"Archivos CSV concatenados y guardados en {archivo_salida}")