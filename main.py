#Desarrollo de script para cruzar los datos de la bibilioteca con el proviemiente en la catedra.
#planiacion del script

#1. Puedo aplicar un ordenamiento rapido (quick sort) a los datos de la catedra y de la biblioteca(ordenar por ISBN). Esto para luego aplicar busqueda binaria.
#2. Aplicar busqueda binaria para buscar los datos de la catedra en la biblioteca.

#Los datos resultante son de todos los años, los de la caatedra son de primer año. ¿Como puedo filtrar los datos de la biblioteca para que solo sean de primer año?--pensasr mas adelante.

from src import ordenamiento
import pandas as pd

if __name__ == '__main__':
    archivo = pd.read_csv('C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_biblioteca.csv', delimiter=',')
    columna = 'isbn'  # Reemplaza con el nombre de la columna que deseas ordenar
    
    # Aplicar Quick Sort al DataFrame
    file = ordenamiento.sorted(archivo, columna)
    
    # Guardar el DataFrame ordenado en un nuevo archivo CSV
    file.to_csv('C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_biblioteca_ordenado.csv', index=False)
   