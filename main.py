#Desarrollo de script para cruzar los datos de la bibilioteca con el proviemiente en la catedra.
#planiacion del script

#1. Puedo aplicar un ordenamiento rapido (quick sort) a los datos de la catedra y de la biblioteca(ordenar por ISBN). Esto para luego aplicar busqueda binaria.
#2. Aplicar busqueda binaria para buscar los datos de la catedra en la biblioteca.

#Los datos resultante son de todos los años, los de la caatedra son de primer año. ¿Como puedo filtrar los datos de la biblioteca para que solo sean de primer año?--pensasr mas adelante.

from src import ordenamiento
import pandas as pd
import plotly.graph_objects as go

# titulos_autores_biblioteca.csv = contiene los titulos y autores de libros disponible en la biblioteca.
# bibliografia_programas_proce = contiene los titulos y autores de las catedras de 1re año disponibles en los programas

# Determinar el porcentaje de libros de la catedra que estan en la biblioteca


# Cargar los datos

csv_catedra = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/bibliografia_programas_proce.xlsx'
csv_biblioteca = 'C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/titulos_autores_biblioteca.csv'

df_catedra = pd.read_excel(csv_catedra)
df_biblioteca = pd.read_csv(csv_biblioteca, delimiter=',')


def disponibilidad(df_catedra,df_biblioteca):
    """ Esta funcion determina el porcentaje de libros para cada carrera separado por asignatura que estan disponible en la biblioteca."""

    listado_carreras = df_catedra['Carrera'].unique()
    for carrera in listado_carreras:
        df_carrera = df_catedra[df_catedra['Carrera'] == carrera]
        conteo_libros_asignatura = df_carrera['Asignatura'].value_counts()
        libros_en_biblioteca = df_carrera.merge(df_biblioteca, on=['titulo', 'autor'], how='inner')
        libros_en_biblioteca.drop(columns=['origen'], inplace=True)
        libros_en_biblioteca.drop_duplicates(inplace=True)
        porcentaje_disponible = (len(libros_en_biblioteca) / len(df_carrera)) * 100
        print(f'Porcentaje de libros de la cátedra que están en la biblioteca para la carrera de {carrera}: {porcentaje_disponible:.2f}%')
        conteo_libros_disponibles_asignatura = libros_en_biblioteca['Asignatura'].value_counts()
        if carrera == 'Tecnicatura Universitaria en Procesamiento y Explotación de Datos':
            carrera = 'TUPED'


        # Crear un DataFrame que contenga ambos conteos
        df_conteo = pd.DataFrame({
            'Total Libros': conteo_libros_asignatura,
            'Libros Disponibles': conteo_libros_disponibles_asignatura
        }).fillna(0)  # Rellenar NaN con 0

        # Crear el gráfico de barras horizontales superpuestas
        # Crear el gráfico de barras horizontales superpuestas
        fig = go.Figure()

        # Añadir barras para 'Total Libros'
        fig.add_trace(go.Bar(
            y=df_conteo.index,
            x=df_conteo['Total Libros'],
            name='Total Libros',
            orientation='h'
        ))

        # Añadir barras para 'Libros Disponibles'
        fig.add_trace(go.Bar(
            y=df_conteo.index,
            x=df_conteo['Libros Disponibles'],
            name='Libros Disponibles',
            orientation='h'
        ))

        # Añadir etiquetas y título
        fig.update_layout(
            title='Disponibilidad de Libros por Asignatura en la Biblioteca en la Carrera: ' + carrera,
            xaxis_title='Número de Libros',
            yaxis_title='Asignatura',
            yaxis=dict(tickmode='linear'),
            barmode='group',
            font=dict(size=18, color='black')  # Agrandar las etiquetas y cambiar el color a negro más fuerte
        )
        #mostrar el grafico
        fig.show()
        # Crear gráfico de torta para la disponibilidad de libros
        fig_pie = go.Figure()

        # Añadir datos al gráfico de torta
        fig_pie.add_trace(go.Pie(
            labels=['Disponibles', 'No Disponibles'],
            values=[porcentaje_disponible, 100 - porcentaje_disponible],
            hole=.3
        ))

        # Añadir título
        fig_pie.update_layout(
            title='Porcentaje de libros  disponibles en la Biblioteca para la Carrera: ' + carrera,
            font=dict(size=18, color='black')  # Agrandar las etiquetas y cambiar el color a negro más fuerte
        )

        # Mostrar el gráfico de torta
        fig_pie.show()



res = disponibilidad(df_catedra,df_biblioteca)


#libros no disponibles o encontrados en biblioteca
# Realizar una combinación (merge) para encontrar los libros de cátedra que no están en la biblioteca
libros_no_disponibles = df_catedra.merge(df_biblioteca, on=['titulo', 'autor'], how='left', indicator=True)
libros_no_disponibles = libros_no_disponibles[libros_no_disponibles['_merge'] == 'left_only']

# Eliminar la columna '_merge' que se añadió durante la combinación
libros_no_disponibles = libros_no_disponibles.drop(columns=['_merge'])

#escribir csv 
libros_no_disponibles.to_csv(':/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/Libros_NO_Disponibles_Biblioteca.csv', index= False)