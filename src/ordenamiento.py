#Algoritmo que ordene los datos de la catedra y de la biblioteca por ISBN
#Usaremos sorted de python

#ordenamiento usando sorted
def sorted(df, column):
    return df.sort_values(by=column)