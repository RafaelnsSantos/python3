#faça uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
import random
import time
#1 parte faz o sorteio de 5 numeros e adiciona na lista numeros temporaria:
def sorteia(numeros):
        print(f"sorteando 5 valores da lista: ",end= '')
        for c in range(5):
            n = random.randint(0,10)
            numeros.append(n)
            print(f"{n}",end= ' ',flush=True)
        time.sleep(0.4)
        print()

     
#2 parte 
def somapar(numeros):
        soma = 0
        for c in numeros:
            if c%2 == 0:
                soma += c
        print(f'somando os valores pares de {numeros}, temos {soma}')

lista = []
sorteia(lista)
somapar(lista)
