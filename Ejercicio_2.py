'''Ejercicio 2
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla '''

import random

numero_magico = 12345679
numero_usuario = random.randint(1, 9)
print("El número usuario es: ",numero_usuario)
n_usuario_x_9 = numero_usuario * 9
print("El número usuario multiplicado por 9 es: ",n_usuario_x_9)
valor_final = numero_magico * numero_usuario
print("El número mágico por el número usuario es: ",valor_final)


