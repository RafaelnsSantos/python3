#faça um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando
# o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
import random
print("| JOGO DO PAR OU IMPAR |")
computador = random.randint(0,10)
soma = 0 
contador_de_vitorias = 0
while True:
    n = int(input("Diga um valor: "))
    par_impar = str(input("PAR OU IMPAR [P/I]: ")).strip().upper()[0]
    soma = n + computador
    if soma % 2 == 0 and par_impar == 'P':
        print(f"Voce jogou {n} e o computador jogou {computador}. total de {soma} sendo par. \nVOCE VENCEU!.")
        contador_de_vitorias += 1
    elif soma %2 == 1 and par_impar == 'I':
        print(f"Voce jogou {n} e o computador jogou {computador}. total de {soma} sendo impar. \nVOCE VENCEU!.")
        contador_de_vitorias += 1

    elif soma % 2 == 1 and par_impar == 'P':
        print(f'Voce jogou {n} e o computador jogou {computador}. total de {soma} sendo impar. \nVOCE PERDEU!.')
        break
    elif soma % 2 == 0 and par_impar == 'I':
        print(f"Voce jogou {n} e o computador jogo {computador}. total de {soma} sendo par. \nVOCE PERDEU!")
        break
print(f"GAME OVER ! VOCE VENCEU {contador_de_vitorias} vezes seguidas.")

