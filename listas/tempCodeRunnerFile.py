import random
tam=int(input('Cuantos numeros'))
vector=[]
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
print(vector.__len__())

for i in range(tam):
    #print('posicion ',i,' elemento ',vector[i])
    if vector[i]%2==0:
        print(vector[i],' es par')
    else:
        print(vector[i],' es impar')
print('funcion len,'len(vector))