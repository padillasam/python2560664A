def progresionNumerica():
    num1=-1
    num2=0
    cont=0
    while num1<num2:
        num1=num2
        num2=int(input('ingrese numero')) 
        cont+=1     
    print('Cantidad de numeros ingresada ',cont)

progresionNumerica()
# while True: 
#     num2=int(input('ingrese numero')) 
#     cont+=1 
#     if num1>num2:
#         break
#     num1=num2

# print('Cantidad de numeros ingresada ',cont)
