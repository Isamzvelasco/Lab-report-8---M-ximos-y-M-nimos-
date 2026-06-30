

#Definir el arreglo de numeros (ejemplo)
arreglo = [10, 95, 110, 90, 40]

#Definimos la funcion menor que recibe el arreglo y devuelve el menor elemento
def menor(arreglo):
    minimo = arreglo[0]

    for valor in arreglo:
        if valor < minimo:
            minimo = valor

    return minimo

print("El menor elemento es:", menor(arreglo))