import time 
def linha(tam=42):
    return "-"*tam
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))   
    print(linha())

def leiaint(n):
    while True:
        try:
            valor = int(input(n))
            return valor
        except (ValueError, TypeError):
            print("\033[0;31mPorfavor digite um numero inteiro valido\033[m")
        except (KeyboardInterrupt):
            print("\n\033[0;31mO usuario preferiu nao informa um numero \033[m ")
            return 3

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c =1 
    # o item vai ir em cada item da lista que esta sendo dada la no programa principal
    for item in lista:
        print(f"\033[0;33m{c}\033[m - \033[36m{item}\033[m")
        c +=1
    print(linha())
    opçao = leiaint("\033[0;33msua opçao -> \033[m")
    return opçao
