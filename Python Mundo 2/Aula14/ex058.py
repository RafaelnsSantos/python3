#molhere o desafio 28 onde o computador vai "pensar" em um numero numero entre 0 e 10. so
#agora o jogador vai tenta adivinhar ate acertar, mostrando no final quantos palpites foram
#necessarios para vencer.
import random
tentativas = 0
mais = 'mais'
menos = 'menos'
pensamento = random.randint(0,10)
escolha_user = int(input("Tente descobrir o numero escolhido pelo computador: "))
while pensamento != escolha_user:
    if escolha_user < pensamento:
        mais = 'mais'
        escolha_user = int(input(" {} ... Digite outro palpite: ".format(mais)))
    elif escolha_user > pensamento:
        menos = 'menos'
        escolha_user = int(input(" {} ... Digite outro palpite: ".format(menos)))
        #'se o palpite nao for igual ao numero ou se o palpite for igual ao numero'
    #if escolha_user != pensamento or escolha_user == pensamento:
    tentativas += 1


print("Voce acertou o computador escolheu {} e voce {}".format(pensamento,escolha_user))
print("E voce acertou com {} tentativas ".format(tentativas))