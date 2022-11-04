import random


list=[]
for i in range(10):
    list.append(10)

lista=[round(random.random()*100) for i in range (10)]
print(lista)

impar=[x for x in lista if x%2!=0]
print(impar)
par=[x for x in lista if x%2==0]
print(par)
parimpar=[0 if x%2==0 else x for x in lista]
print(parimpar)


board = []
for i in range(5):
    #row = [[] for i in range(3)]
    board.append([])
print(board)

board = [[] for i in range(3)] 
print(board)
