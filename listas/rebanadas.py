import random
"""
lista1 = [10, 8, 6, 4, 2]
lista2=lista1
nueva = lista1[:2]
nueva.append(5)
print(lista1)
print(nueva)
"""

temp=[]
for i in range(30):
    temp.append(round(random.randint(4,30)))
    print(i)
print(temp)
m1=temp[:15]
m2=temp[15:30]
print(temp[:16])
print(temp[16:])
s1,s2=0,0
for i in range(len(m1)):
    s1=s1+m1[i]
    s2=s2+m2[i]
print('Promedio m1=',(s1/len(m1)))
print('Promedio m2=',(s2/len(m2)))
