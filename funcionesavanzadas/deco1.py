def decoradora(funcion):
    print('inicia función decoradora')
    def acondicionamiento():
        #print(funcion())
        return f'trotar y estirar \n {funcion()}'
    return acondicionamiento

def tapar():
    return 'tapando'
    #print('tapando')

arquero=decoradora(tapar)
print(arquero())

@decoradora
def patear():
    return 'pateando'
print(patear())

@decoradora
def cabecear():
    return 'cabeceando'
print(cabecear())