#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO".
cidade = str(input("digite qual cidade voce nasceu: ")).strip()
s = 'SANTO' in cidade.upper()

print(s)
