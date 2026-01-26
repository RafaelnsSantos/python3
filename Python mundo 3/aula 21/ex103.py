#faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='',gols= 0):
    if nome == '':
        nome = "<desconhecido>"
    if str(gols).isnumeric() : 
       gols = int(gols)
    else:
        gols = 0
    print(f"o jogador {nome} fez {gols} gol(s) no campeonato")



jogador = str(input("Nome do jogador:")).strip()
gol = str(input("numeros de gols: ")).strip()
ficha(jogador,gol)