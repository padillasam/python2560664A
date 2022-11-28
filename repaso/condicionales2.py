import random
a=int(random.randrange(100))
b=int(random.randrange(100))
c=int(random.randrange(100))
print(a,' ',b,' ',c)
#---------------------------
def evaluarIgualdad(x,y,z):
    if x==y and y==z:
        print('Los tres son iguales')
    elif x==y or x==z or y==z:
        print('Dos de ellos son iguales')
    else:
        print('Todos son diferentes')
#--------------------------------
evaluarIgualdad(a,b,c)