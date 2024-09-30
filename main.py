#Desarrollo de script para cruzar los datos de la bibilioteca con el proviemiente en la catedra.
#planiacion del script

#1. Puedo aplicar un ordenamiento rapido (quick sort) a los datos de la catedra y de la biblioteca(ordenar por ISBN). Esto para luego aplicar busqueda binaria.
#2. Aplicar busqueda binaria para buscar los datos de la catedra en la biblioteca.

#Los datos resultante son de todos los años, los de la caatedra son de primer año. ¿Como puedo filtrar los datos de la biblioteca para que solo sean de primer año?--pensasr mas adelante.

def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Partición # utilizando el esquema de partición Lomuto
def partition(a, start, end):
 
    # Elija el elemento más a la derecha como pivote de la lista
    pivot = a[end]
 
    # Los elementos # menores que el pivote serán empujados a la izquierda de `pIndex`
    # Los elementos # más que el pivote se empujarán a la derecha de `pIndex`
    # elementos iguales pueden ir en cualquier dirección
    pIndex = start
 
    # cada vez que encontramos un elemento menor o igual que el pivote,
    # `pIndex` se incrementa, y ese elemento se colocaría
    # antes del pivote.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1
 
    # swap `pIndex` con pivote
    swap(a, end, pIndex)
 
    # devuelve `pIndex` (índice del elemento pivote)
    return pIndex
 
 
# Rutina de clasificación rápida
def quicksort(a, start, end):
 
    # Condición base
    if start >= end:
        return
 
    # reorganizar elementos a través de pivote
    pivot = partition(a, start, end)
 
    # recurre en la sublista que contiene elementos menores que el pivote
    quicksort(a, start, pivot - 1)
 
    # recurre en la sublista que contiene más elementos que el pivote
    quicksort(a, pivot + 1, end)
 
 
# Implementación en Python del algoritmo Quicksort
if __name__ == '__main__':
 
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
    quicksort(a, 0, len(a) - 1)
 
    # imprime la lista ordenada
    print(a)