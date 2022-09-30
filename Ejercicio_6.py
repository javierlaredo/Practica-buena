'''Ejercicio 6
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
[2, 6]
[1, 5, 7]
Sugerencia
Para ordenar una lista automáticamente puedes utilizar el método .sort().
'''

def separar(numeros):
    lista = [6, 5, 2, 1, 7] 
    pares = []
    impares = []
    for numeros in lista:
        if numeros % 2==0:
           pares.append(numeros)
        else:
            impares.append(numeros)
    return pares, impares

pares, impares = separar([])
print(pares)
print(impares)
