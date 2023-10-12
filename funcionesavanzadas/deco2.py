def decoradora(funcion):
    print('inicia la decoración')
    def interna(*args,**kwargs):
        print(funcion(*args,**kwargs))
    return interna    

@decoradora
def suma(num1,num2):
    return num1+num2

@decoradora
def suma3(num1,num2,num3):
    return num1+num2+num3

suma3(5,9,4)