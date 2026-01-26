
#faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
#quer tambem informar quantos valores foram passados para a função maior().
import time
def maior(*valores):#valores e uma tupla
    cont = maior = 0
    print("Analisando os valores...")
    time.sleep(0.5)  
    for c in valores:
        print(f'{c}',end= ' ', flush= True)
        time.sleep(0.5)
        if cont == 0:
            maior = c 
        else:
            if c > maior:# se c for maior que maior # c percore todos os valores
                maior = c #maior recebe c 
        cont += 1
    print(f'foram informados {cont} valores ao todo.')
    print(f'o maior valor informado foi: {maior}') 
    print('-='*30)

print('-='*30)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
