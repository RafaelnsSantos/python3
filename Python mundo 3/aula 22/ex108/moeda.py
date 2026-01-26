def aumentar(preço,taxa=10):
    porcentagem = preço + (preço*taxa)/100
    return porcentagem

def diminuir (preço,taxa=10):
    porcentagem = preço - (preço*taxa)/100
    return porcentagem

def dobro(preço):
    aumento = preço*2
    return aumento

def metade(preço):
    meio = preço/2
    return meio

def moeda (a):
    return f'{a:.2f}'.replace('.',',')

#com o guanabara:
#def moeda (preço = 0 , moeda = "R$"):
#   return f " {meoda} {preço} ".replace(".",",")
    
