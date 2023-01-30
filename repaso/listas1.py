def llenadoLista(lista,limite):
    i=0
    while i<limite:
        lista.append(i) 
        i+=1
    return lista

print(llenadoLista([],6))


def llenarLista(lista,limite):
    for i in range(limite):
        lista.append(i)
    return lista

l=llenarLista([],-10)
print(l)


