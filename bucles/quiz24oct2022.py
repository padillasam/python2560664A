n=int(input('Ingrese numero'))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

bac=int(input('Ingrese poblacion inicial'))
bac1=bac*2
p=float(input('Ingrese porcentaje de crecimiento'))
while bac<bac1:
    print('bac',bac)
    bac=bac+(bac*p)
    print('Bacterias= ',bac)
