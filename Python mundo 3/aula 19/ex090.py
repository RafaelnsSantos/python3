#faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.
boletim = {}
nome = str(input("Nome do aluno: ")).strip()
media = float(input("Digite a media do aluno: "))

boletim['aluno'] = nome
boletim['media'] = media

if media < 5:
    boletim['situaçao'] =  'reprovado'
elif media <= 7:
    boletim['situaçao'] = 'recuperaçao'
elif media > 7:
    boletim['situaçao'] = 'Aprovado'

for k , v in boletim.items():
    print(f"{k} e igual a {v}")