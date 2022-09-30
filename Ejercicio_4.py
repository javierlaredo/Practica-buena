'''Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.'''

def ordenar(c):
    return c['prioridad']

cola = [
    {'tarea1': 'Redactar', 'prioridad':3},
    {'tarea2': 'Investigar', 'prioridad':1},
    {'tarea3': 'Escribir', 'prioridad':2},
    {'tarea4': 'Jugar', 'prioridad':4}

]
print(cola)
cola.sort(key=ordenar)
n = cola.pop(0)['tarea2']

print(f"Lo más prioritario es: {n}")