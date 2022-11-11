
def sumaDivisores(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

def perfecto(n):
    suma=sumaDivisores(n)
    if n==suma:
        return 'perfecto'
    else:
        return 'No es perfecto'

def primo(n):
    suma=sumaDivisores(n)
    if suma==1:
        return 'primo'
    else:
        return 'No es primo'

def amigos(x,y):
    sumx=sumaDivisores(x)
    sumy=sumaDivisores(y)
    if sumx==y and sumy==x:
        return 'Son amigos'
    else:
        return 'No son amigos'

print(amigos(220,284))
#print(sumaDivisores(23))
#print(perfecto(28))
print(primo(100))