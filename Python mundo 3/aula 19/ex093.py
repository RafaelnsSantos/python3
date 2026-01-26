#crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
#  tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
#  O programa também deve mostrar o conteúdo da estrutura na tela.

campeonato = {}
listagols = []
cont = 0
somagols = 0
jogador = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas o {jogador} jogou? "))

for c in range (partidas):
    gols = int(input(f"Quantos gol ele fez na {c + 1} partida: "))
    listagols.append(gols)
    somagols += gols

campeonato['jogador'] = jogador
campeonato['partidas'] = partidas
campeonato['gols'] = listagols
campeonato['total gols:'] = somagols 

for k , c in campeonato.items():
    print(f"{k} = {c}")
print(f"O jogador {jogador} jogou {partidas} Partidas. ")


for c in campeonato['gols']:
    cont += 1
    print(f"=> Na partida {cont}, fez {c} gols")
print(f"Total de {campeonato['total gols:']} gols")


