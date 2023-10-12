def sumar(num1,num2):
    return num1+num2


def posicionales(*args):
    #print(type(args))
    s=0
    for i in args:
       s+=i
    return s

print(posicionales(10,20,30))

# adso={
#     'ficha':'2560664A',
#     'ambiente':206
# }

def clave(**kwargs):
    #print(type(kwargs))
    for x,y in kwargs.items():
        print(f'{x}:{y}')
        #print(x,':',y)

clave(num1=10,num2=20,nombre='ana',edad=25)


def myfunction(*args,**kwargs):
    pass

myfunction(1,2,3,nombre="pedro",edad=28)
