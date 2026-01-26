def aumentar (preço,taxa=10 , show = False):
    porcentagem = preço + (preço*taxa)/100
    return porcentagem if show is False else moeda(porcentagem)
    
def diminuir (preço,taxa=10,show = True):
    porcentagem = preço - (preço*taxa)/100
    return porcentagem if show is False else moeda(porcentagem)

def dobro(preço,show=True):
    aumento = preço*2
    return aumento if show is False else moeda(aumento)

def metade(preço,show=True):
    meio = preço/2
    return meio if show is False else moeda(meio)

def moeda (preço= 0, moeda = "R$"):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
