#Desarrollo de script para cruzar los datos de la bibilioteca con el proviemiente en la catedra.
#planiacion del script

#1. Puedo aplicar un ordenamiento rapido (quick sort) a los datos de la catedra y de la biblioteca(ordenar por ISBN). Esto para luego aplicar busqueda binaria.
#2. Aplicar busqueda binaria para buscar los datos de la catedra en la biblioteca.

#Los datos resultante son de todos los años, los de la caatedra son de primer año. ¿Como puedo filtrar los datos de la biblioteca para que solo sean de primer año?--pensasr mas adelante.

import pandas as pd

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

if __name__ == '__main__':
    archivo = pd.read_csv('C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_biblioteca.csv', delimiter=',')
    columna = 'isbn'  # Reemplaza con el nombre de la columna que deseas ordenar
    
    # Convertir la columna en una lista
    lista = archivo[columna].tolist()
    
    # Aplicar quicksort a la lista
    quicksort(lista, 0, len(lista) - 1)
    
    # Reemplazar la columna original con la lista ordenada
    archivo[columna] = str(lista)
    
    # Guardar el DataFrame ordenado en un nuevo archivo CSV
    archivo.to_csv('C:/Users/Axel/Desktop/Practica-Biblioteca/data/procesados/libros_biblioteca_ordenado.csv', index=False)