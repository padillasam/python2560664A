flujo=open('archivos/inicio1.txt','a+')
#r+ hace update y lee
#a+ hace update pero no lee
#datos=flujo.read()
#print(datos)
datos=flujo.read()
print(datos)
flujo.write('\nCuando estudian con juicio----')
flujo.close()