#desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final mostre os 10
#primeiros termos dessa progressao

termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
for c in range(10):
    print(termo)
    termo += razao
# inicio  e  fim e o pulo no caso: a razao ex:  termo= 0 razao = 2
#começa com 0 e vai ate comprir o range, de 2 em 2 no caso o range e 10 para comprir os 10 primeiros termos
#0 2 4 6 8 10 12 14 16 18
