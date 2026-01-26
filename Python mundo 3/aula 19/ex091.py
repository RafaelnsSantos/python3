#crie um progrma onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, 
#sabendo que o vencedor tirou o maior número no dado.
import random
resultado = {}
cont = 0
jogador1 = random.randint(1,6)
jogador2 = random.randint(1,6)
jogador3 = random.randint(1,6)
jogador4 = random.randint(1,6)
resultado['jogador1'] = jogador1
resultado['jogador2'] = jogador2
resultado['jogador3'] = jogador3
resultado['jogador4'] = jogador4

print("Valores sorteados: ")
for v , c in resultado.items():
    print(f"O {v} tirou {c}")
print("Raking dos jogadores: ")
#uma forma de organizar de forma decrescente um dicionario e usando o dict adjunto do sorted assim organizando

resultado = dict(sorted(resultado.items(), key = lambda item: item[1], reverse=True))
for v , c in resultado.items():
    cont+= 1
    print(f"{cont} Lugar: {v} com {c}") 
#soluçao do professor
'''from operator import itemgetter
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")'''
