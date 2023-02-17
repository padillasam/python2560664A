def abc(cad):
    cont=0
    vacia=''
    for i in cad:
        if i not in vacia:
            vacia+=i
    return len(vacia)

print(abc('sena soacha'))
