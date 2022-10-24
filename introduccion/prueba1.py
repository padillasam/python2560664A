from re import U
from socketserver import UDPServer


user=input('Aprendizaje de python, cual es su nombre\n')
print('bienvenido ',user)
lang=input('Favorite programming language')
#print(lang,'is','fun',sep='*',end='!....\n');
print(lang,'is','fun',sep='*',end='\n');

#desagregar numero en digitos

n=234
u=n%10
n=n//10
d=n%10
n=n//10
c=n%10
print(u,d,c)

#CONTADORES ACUMULADORES
#var=var+constante
suma=suma+var
