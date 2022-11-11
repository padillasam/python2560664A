import random
def sumLista(lista):
    sum=0
    for i in lista:
        sum+=i
    return sum

def llenarLista(lista):
    tam=round(random.randint(5,15))
    for i in range(tam):
        lista.append(round(random.randrange(100)))
    return lista

list=[]
list=llenarLista(list)
print(list)
print(sumLista(list))

