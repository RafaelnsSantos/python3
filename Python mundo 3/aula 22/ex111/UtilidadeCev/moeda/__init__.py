def aumentar (preço,taxa=10 , show = False):
    """
    calcula o aumento de um terminado preço
    retornando o resultado com ou sem formataçao no preço
    :param preço: preço que voce quer se reajustado
    :param taxa: a porcetagem para aumento do preço
    :param show: mostra sem ou com formataçao
    :return: o valor rejustado
    """
    porcentagem = preço + (preço*taxa)/100
    return porcentagem if show is False else moeda(porcentagem)
    
def diminuir (preço,taxa=10,show = False):
    porcentagem = preço - (preço*taxa)/100
    return porcentagem if show is False else moeda(porcentagem)

def dobro(preço,show=False):
    aumento = preço*2
    return aumento if show is False else moeda(aumento)

def metade(preço,show=False):
    meio = preço/2
    return meio if show is False else moeda(meio)

def moeda (preço= 0, moeda = "R$"):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def escreva (txt):
    adaptaçao = len(txt)
    print("-"*30)
    print(f"{txt}".center(30))
    print("-"*30)


def resumo(preço=0,taxa=10,taxa2=5):
    escreva("RESUMO DO VALOR")
    print(f"preço analisado:   \tR${preço}")
    print(f"Dobro do preço:   \t{dobro(preço,True)}")
    print(f"metade do preço:  \t{metade(preço,True)}")
    print(f"{taxa} de aumento:   \t{aumentar(preço,taxa,True)}")
    print(f"{taxa2} de reduçao:  \t{diminuir(preço,taxa2,True)}")
    print("-"*30)

