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
import pandas as pd
import matplotlib.pyplot as plt
# Cargar los datos

csv_catedra = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/bibliografia_programas_proce.xlsx'
csv_biblioteca = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/titulos_autores_biblioteca.csv'

df_catedra = pd.read_excel(csv_catedra)
df_biblioteca = pd.read_csv(csv_biblioteca, delimiter=',')


df_tuped = df_catedra[df_catedra['Carrera'] == 'Tecnicatura Universitaria en Procesamiento y Explotación de Datos']

print(df_tuped)

# Realizar la combinación para encontrar los libros de df_tuped que están en df_biblioteca
libros_en_biblioteca = df_tuped.merge(df_biblioteca, on=['titulo', 'autor'], how='inner')

print(libros_en_biblioteca)

# Porcentaje de libros de la cátedra que están en la biblioteca para la carrera de TUPED
porcentaje_disponible_tuped = (len(libros_en_biblioteca) / len(df_tuped)) * 100


# Contar el número de libros por asignatura en df_tuped
conteo_libros_asignatura = df_tuped['Asignatura'].value_counts()


#elimino las columnas que no necesito
libros_en_biblioteca.drop(columns=['origen'], inplace=True)
#eliminos filas duplicadas
libros_en_biblioteca.drop_duplicates(inplace=True)


# Contar el número de libros disponibles por asignatura en libros_en_biblioteca
conteo_libros_disponibles_asignatura = libros_en_biblioteca['Asignatura'].value_counts()

# Crear un DataFrame que contenga ambos conteos
df_conteo = pd.DataFrame({
    'Total Libros': conteo_libros_asignatura,
    'Libros Disponibles': conteo_libros_disponibles_asignatura
}).fillna(0)  # Rellenar NaN con 0

# Crear el gráfico de barras superpuestas
ax = df_conteo.plot(kind='bar', figsize=(10, 6))

# Añadir etiquetas y título
ax.set_xlabel('Asignatura')
ax.set_ylabel('Número de Libros')
ax.set_title('Conteo de Libros por Asignatura y Disponibilidad en Biblioteca')
# Rotar las etiquetas del eje x
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
# Mostrar el gráfico
plt.show()

libros_en_biblioteca.to_csv('C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_en_bibliotecatuped.csv', index=False)
df_tuped.to_csv('C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_tuped.csv', index=False)