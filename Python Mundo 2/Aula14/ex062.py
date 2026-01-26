#Melhore o desafio 061 perguntando para o usuario se ele quer mostra mais alguns termos. o
#programa encerra quando ele disser 0 
termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
print("{}".format(termo), end= ' ')
co = 1 # e um acumulador 
t = 10
total = 0 
#repita em quanto t e indiferente de 0 
while t != 0: # ta funcionando 
    total += t
    while co < t:
        co += 1
        termo += razao
        print("{}".format(termo),end = ' ')
    t = int(input("\nQuantos termos voce quer mais? "))
    co = 0
print("progressao finalizada com {} termos mostrados".format(total))