#faça um programa que tenha uma funçao chamada contador(), que receba três parâmetros: início, fim e passo.
#e realize a contagem. seu programa tem que realizar três contagens através da funçao criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

#minha resoluçao:
import time
def contador (inicio, fim , passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("-=-"*15)
    print(f'contagem de {inicio} ate {fim} de {passo} de {passo}')
    time.sleep(1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}",end= ' ',flush= True)
            cont += passo
            time.sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}",end= ' ',flush= True)
            time.sleep(0.5)
            cont -= passo
        print("-=-"*15)
        
#programa principal
contador(1,10,1)
contador(10,0,2)
print("agora voce pode fazer sua contagem: ")
contador(inicio=int(input('Inicio: ')), fim=int(input('fim:')), passo=int(input("passo:")))





#resolução do guanabara
'''def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= passo
        print('FIM!')'''


