#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada 
#jogo, cadastrando tudo em uma lista composta.
import random
print("-=-"*7)
print("|   NUMEROS DA MEGA |")
print("-=-"*7)
jogos = []
escolha_user = int(input("Quantos jogos voce que eu sorteie? "))
for c in range(escolha_user):
    linha = []
    #ele vai gerar 6 numeros e vai checar se esses numeros ja nao estao em linha se nao tiver ele adiciona
    while len(linha) < 6:
        numero = random.randint(1,60)
        if numero not in linha:
            linha.append(numero)
    jogos.append([linha])
    
print(f"-=-=-= SORTEANDO {c+1} JOGOS -=-=-=-" )
#i vai percorer linha 
for i , linha in enumerate(jogos):
    print(f"Jogo: {i+1}:{sorted(linha)}")
