#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário
#possa mostrar as notas de cada aluno individualmente.
alunos = []
media = 0
while True:
    nome = str(input("Digite o nome do aluno: ")).strip()
    nota = float(input("Digite 1 nota: "))
    nota2 = float(input("Digite 2 nota: "))
    media = (nota + nota2) / 2     #3
    alunos.append([nome,[nota,nota2],media])
    #                        0
    escolha_user = ' '
    while escolha_user != 'SN':
        escolha_user = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        if escolha_user in 'SN':
            break

    if escolha_user == 'N':
        break
print("-=-"*13)
print("No.  NOME          MEDIA")
print("---"*13)
for p, c in enumerate(alunos):
    print(f"{p+1}   {c[0]}         {c[2]}")

while True:
    boletim_escolha = int(input("Mostra nota de qual aluno?(999 para interrompe) "))
    if boletim_escolha == 999:
        break

    elif 1 <= boletim_escolha <= len(alunos):
        aluno = alunos[boletim_escolha - 1]
        print(f"Notas de {aluno[0]} sao: {aluno[1]}")
    else:
        print("Aluno invalido")
