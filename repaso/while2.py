def factoresPrimos(num):
    div=2
    while div<=num:
        if num%div==0:
            print(div)#2,
            num/=div#num=num/div
        else:
            div+=1

num=int(input('ingrese numero')) 
factoresPrimos(num)