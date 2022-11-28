import random
#intervalo=int(random.randint(-100,100))
x=int(random.randint(-100,100))
y=int(random.randint(-100,100))
if x<0:
    x*=-1
    print('x era negativo')
elif y<0:
    y*=-1
    print('y era negativo')
print('x= ',x)
print('y= ',y)
if x<y:
    x,y=y,x
if x%y==0:
    print(x,'es multiplo de ',y)
else:
    print(x,'No es multiplo de ',y)


