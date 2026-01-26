#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. depois disso, mostre a listagem de numeros
#gerados e tambem indique o menor e o maior valor que estao na tupla 
import random

tupla = random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)
#maior = tupla[0]
#menor = tupla[0]

#forma simples de comparaçao quando tem varios valores para comparar e atribuir maior ou menor 
#o c vai percorer pela tupla e vai ir comparando.
#for c in tupla:
    #if c > maior:
        #maior = c
    #elif c < menor:
        #menor = c

#FORMA MAIS FACIL:
print(f'valores sorteados: {tupla}\nO maior valor {max(tupla)}\nMenor valor {min(tupla)}') 