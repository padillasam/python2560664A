import random
year=int(random.randint(1200,3000))
print(year)
#--------------------------
def bisiesto(anio):
    if anio%400==0:
        print('es bisiesto')
    elif anio%100==0:
        print('No es bisiesto')
    elif anio%4==0:
        print('es bisiesto')
    else:
        print('No es bisiesto')
#-------------------------------
bisiesto(year)