dict = {"gato" : "cat", "perro" : "dog", "caballo" : "horse"}
#método get
print(dict.get('gato'))
print(dict['gato'])

#eliminar
del dict['perro']
print(dict)

#update
#dict['pollo']='chicken'
dict.update({'pollo':'chicken'})
dict['pato']='duck'
print(dict)
#metodo popitem
#dict.popitem()

#método items()
for esp, en in dict.items():
    print(esp,'->',en)

#metodo values()
for x in dict.values():
    print(x)

for y in dict.keys():
    print(y)

