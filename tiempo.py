def segundo_a_minuto(segundo):
    return segundo /60 

if __name__=="__main__":
    segundo = 150 
    minutos = segundo_a_minuto(segundo)
    print(f"{segundo} segundos equivalen a {minutos} minutos")
    