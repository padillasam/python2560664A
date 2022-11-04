lista=[10,5,2,7,5,3]
for i in lista:
    print(i)
num=100
print (not(num not in lista))



my_list = [17, 3, 111, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)
vec=[]
for i in my_list:
    if i not in vec:
        vec.append(i)
print(vec)


print("La lista con elementos únicos:")
print(my_list)

#Eliminacion elementos lista
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # salida: [3, 4, 5]

del my_list[:]
print(my_list)  # delimina el contenido de la lista, genera: []

