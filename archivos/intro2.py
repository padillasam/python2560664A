#flujo=open('archivos/inicio.txt','a+')
with open('archivos/inicio.txt','r+') as flujo:
    datos=flujo.read()
    print(datos)
