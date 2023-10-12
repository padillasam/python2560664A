def base(p_base):
    print(f'{p_base} inicia base')
    def interna(p_interna,p_base):
        #print('codigo de la funcion interna')
        print(f'{p_interna} interna')
        print(f'{p_base} fin base')
    return interna

recibe_interna=base(100)
recibe_interna(5,10)
recibe_interna(5,11)
recibe_interna(5,12)
recibe_interna(5,13)
