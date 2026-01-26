#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.
nome = str(input("Digite seu nome completo: ")).strip()
s = 'silva' in nome.lower()

print("seu nome tem silva? {}".format(s))