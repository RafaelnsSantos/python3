# A Confederaçao Nacional de nataçao precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria de acordo com a idade: 0 - 9 mirim, 14 infatil , 19 junior ,20 senior , acima master
from datetime import date
print("-=-"*15)
print("programa da confederaçao nacional de nataçao")
print("-=-"*15)
nome = str(input("Qual o nome do(a) nadador(a): "))
ano = int(input("Qual sua data de nascimento? "))
atual = date.today().year
calculo = atual - ano
if calculo <= 9:
    print("A Categoria do(a) Nadador(a) {} e MIRIM ".format(nome))
    print("tem {} anos".format(calculo))
elif calculo <= 14:
    print("A Categoria do(a) Nadador(a) {} e INFATIL ".format(nome))
    print("tem {} anos".format(calculo))
elif calculo <= 19:
    print("A Categoria do(a) Nadador(a) {} e JUNIOR ".format(nome))
    print("tem {} anos".format(calculo))
elif calculo <= 25:
    print("A Categoria do(a) Nadador(a) {} e SENIOR ".format(nome))
    print("tem {} anos".format(calculo))
else:
    print("A Categoria do(a) Nadador(a) {} e MASTER ".format(nome))
    print("tem {} anos".format(calculo))