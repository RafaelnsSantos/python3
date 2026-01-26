#refaça o desafio 51, lendo o primeiro termo e a razao de uma PA mostrando os 10 primeiros
#termos da progressao usando a estrutura while 
#co e um contador 
termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
print("{}".format(termo), end= ' ')
co = 1
while co < 10:
    co += 1
    termo += razao
    print("{}".format(termo),end = ' ')
