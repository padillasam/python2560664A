while True:
    print('1-ingresar cancion')
    print('2-ingresar artista')
    print('3-Eliminar artista')
    print('5-salir')
    ctrl=int(input('Ingrese la opcion'))
    match ctrl:
        case 1:
            print('ingreso 1')
        case 2:
            print('ingreso 2')
        case 3:
            print('ingreso 3')
        case 4:
            print('ingreso 4')
        case 5:
            print('ingreso 5')
        case _:
            print('no existe')


"""
if ctrl==1:
    print('Selecciono uno')
    #ingresarcancion()
elif ctrl==2:
    print('Selecciono dos')
elif ctrl==3:
    print('Selecciono tres')
else:
    print('no existe la opcion')
"""