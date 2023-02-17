def ortografia(c):
    if(c[-1]==chr(225) or c[-1]==chr(233) or c[-1]==chr(237) or c[-1]==chr(243) or c[-1]==chr(250)):
        print('Aguda')
    else:
        print('No es aguda')

ortografia('café')