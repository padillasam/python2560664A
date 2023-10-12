import random

def base(funcion):
    print('Primera línea de la función base')
    print(funcion())
    print('Línea final de la función base')

def generar_lista():    
    print([random.randint(0, 100) for _ in range(random.randint(10, 100))])

def trivial():
    return 'Hola adso Soacha'

base(generar_lista)
base(trivial)
