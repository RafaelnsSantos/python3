#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
#No final de acordo com sua media atingida: - media abaixo de 5 reprovado , media 5 - 6.9 recuperaçao
#media 7 aprovado!
print("-=-"*7)
print("| Escola santa bela |")
print("-=-"*7)
nome = str(input("Nome do aluno(a)"))
n1 = float(input("Primeira nota do aluno(a) {} : ".format(nome)))
n2 = float(input("Segunda nota do aluno(a)  {} : ".format(nome)))
#n3 = float(input("Terceira nota do aluno(a) {} : ".format(nome)))
media = (n1+n2)/2
if media < 5:
    print("Aluno(a): {} Esta com media {:.1f}".format(nome,media))
    print("Reprovado")
elif media <= 6.9:
    print("Aluno(a): {} Esta com media {:.1f}".format(nome,media))
    print("recuperaçao")
elif media >= 7:
    print("Aluno(a): {} Esta com media {:.1f}".format(nome,media))
    print("Aprovado!")
