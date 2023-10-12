def decoradora(funcion):
    print('inicia función decoradora')
    def acondicionamiento():
        #print(funcion())
        return f'trotar y estirar {funcion()}'

    return acondicionamiento

def tapar():
    return 'tapando'
    #print('tapando')

#arquero=decoradora(tapar)
#print(arquero())

@decoradora
def patear():
    return 'pateando'

print(patear())