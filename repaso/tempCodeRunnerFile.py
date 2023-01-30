def llenadoLista(lista,limite):
    i=0
    while i<limite:
        lista.append(i) 
        i+=1
    return lista

print(llenadoLista([],6))