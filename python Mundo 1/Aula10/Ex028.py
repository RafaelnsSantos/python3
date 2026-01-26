#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 a peça para o usuário 
#tentar descobrir qual foi o número escolhido palo computador.
#O programa deverá escrever na tala se O usuário venceu ou perdeu
import random
print("="*30)
print("|      JOGO DA SORTE         |")
print("="*30)
escolha_user = int(input("Tente descobrir o numero escolhido pelo computador: "))
pensamento = random.randint(0,5)#faz o computador pensar 
if escolha_user == pensamento:
    print("O computador escolheu {} Parabens! Voce venceu o jogo".format(pensamento))
else:
    print("O computador escolheu {} Voce perdeu".format(pensamento))

    #extra na resoluçao e usar a biblioteca time usando o metodo sleep fazendo o 
    # 'computador ' esperar 
