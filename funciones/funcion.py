def impresion():
    for i in range(10):
        print('2560664A los mejores programadores del SENA')

def saludo(nombre, programa):
    print('Hola ',nombre, 'pertenece a ',programa)

saludo('Maria','Contabilidad')
saludo('ana','adso')
saludo('pedro','adsi')
saludo(1,2)

import random
def parimpar(num):
    if num%2==0:
        #print('par')
        return 'par'
    else:
        #print('impar')
        return 'impar'

lista=[]
for i in range(10):
    lista.append(round(random.randrange(100)))
print(lista)
for i in lista:
    print(i)
    #dato=parimpar(i)
    #len(dato)
    print(parimpar(i))






