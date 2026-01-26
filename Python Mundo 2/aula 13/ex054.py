#criei um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
#ainda nao atigiram a maior idade e quantas ja sao maiores
from datetime import date
atual = date.today().year 
cont_18 = 0
cont_17 = 0
for c in  range(1,8):
    ano = int(input("ano de nascimento da {} Pessoa: ".format(c)))
    idade = atual - ano
    if idade >= 18:
        cont_18 += 1
    else:
        cont_17 += 1
print("{} pessoas ja sao maiores de idade \nE {} pessoas ainda sao de menores ".format(cont_18,cont_17))
