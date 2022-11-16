tupla=(1,2,3,4,5,6)
for i in tupla:
    print(i)

print(tupla[:3])
tupla+=(1,)
print(tupla)
lista=[]
lista=tupla
print(lista)
lista2=list(tupla)#casting
print(lista2)

import random
tup=tuple(round(random.random()*100) for i in range (10))
print(tup)