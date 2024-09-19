
import pandas as pd
from src.lectura import leer_csv

#libros de material de consulta
df_libros_consulta = pd.read_csv('Archivos/libros (mat de consulta) total en Koha al 2_9_2024.csv', delimiter=';') 
#libros total en koha 
df_libros_total = pd.read_csv('Archivos/ANALISIS DE COLECCIÓN - PRUEBA -reportresults.csv', delimiter=';')
#libros en bidi
df_libros_bidi = pd.read_csv('Archivos/libros vigentes en bidi al 2_9_2024.csv', delimiter=';')

#-------------------------------------------------------------------------------------------------------------------------------
#BASE DE DATOS BIDI
# Asignar nombres de columnas a la base de datos bidi ya que no cuenta con esto
df_libros_bidi.columns = ['ID', 'Titulo', 'Autor', 'isbn', 'Editorial','Universidad','Numero_licencia','dato','Fecha_vencimiento_lic'] 
#print(df_libros_bidi.head())
df_libros_bidi_ = df_libros_bidi[['ID', 'Titulo', 'Autor', 'isbn', 'Editorial','Fecha_vencimiento_lic']]
print(df_libros_bidi_.head())

#-------------------------------------------------------------------------------------------------------------------------------
#BASE DE DATOS SOBRE EL MATERIAL DE CONSULTA KOHA
print(df_libros_consulta.head())
df_libros_consulta_ = df_libros_consulta[['barcode','title','author','isbn']]
print(df_libros_consulta_.head(50))


#-------------------------------------------------------------------------------------------------------------------------------
#BASE DE DATOS TOTAL KOHA
print('aaaaaaa')
print(df_libros_total.head())
df_libros_total_ = df_libros_total[['barcode','title','author','isbn']]
print(df_libros_total_.head(50))