#Algoritmo que ordene los datos de la catedra y de la biblioteca por ISBN
#Usaremos sorted de python

import pandas as pd

# Función de partición
def partition(df, low, high, column):
    pivot = df.loc[high, column]  # Escogemos el pivote
    i = low - 1
    
    for j in range(low, high):
        if df.loc[j, column] < pivot:
            i += 1
            # Intercambiamos las filas i y j
            df.iloc[i], df.iloc[j] = df.iloc[j].copy(), df.iloc[i].copy()
    
    # Intercambiamos el pivote con el elemento después del último menor que el pivote
    df.iloc[i+1], df.iloc[high] = df.iloc[high].copy(), df.iloc[i+1].copy()
    
    return i + 1

# Función recursiva de Quick Sort
def quick_sort(df, low, high, column):
    if low < high:
        pi = partition(df, low, high, column)
        
        # Ordenamos las dos mitades
        quick_sort(df, low, pi - 1, column)
        quick_sort(df, pi + 1, high, column)

# Crear un DataFrame de ejemplo
data = {
    'isbn': ['978-3-16-148410-0', '978-0-306-40615-7', '978-0-123-45678-9', '978-1-86197-876-9'],
    'title': ['Book A', 'Book B', 'Book C', 'Book D']
}
df = pd.DataFrame(data)

# Aplicar Quick Sort a la columna 'isbn'
quick_sort(df, 0, len(df) - 1, 'isbn')

print(df)

#ordenamiento usando sorted
def sorted(df, column):
    return df.sort_values(by=column)