#Criei um programa que faça o computador jogar jokenpo com voce.
import random
print("-=-"*4)
print("|  JOKENPO |")
print("-=-"*4)
computador = random.randint(1,3)
print("[1] PEDRA \n[2]PAPEL \n[3]TESOURA")
escolha = int(input("Escolha: "))
if  (computador == 1  and escolha == 2 ): 
    print("O computador escolheu pedra e voce papel")
    print("Voce venceu")
elif  (computador == 2 and escolha == 3):
    print("O computador escolheu papel e voce tesoura")
    print("Voce venceu")
elif  (computador == 3 and escolha == 1):
    print("O computador escolheu tesoura e voce pedra")
    print("Voce venceu")

elif( computador == 1 and escolha == 3): 
    print("O computador escolheu pedra e voce escolheu tesoura")
    print("Voce perdeu!")
elif(computador == 2 and escolha == 1):
    print("O computador escolheu papel e voce pedra") 
    print("voce perdeu")
elif(computador == 3 and escolha == 2):
    print("O computador escolheu tesoura e voce papel")
    print("Voce Perdeu!")
elif (computador == 1 and escolha == 1) or (computador == 2 and escolha ==2 ) or (computador == 3 and escolha == 3 ):
    print("Empate")