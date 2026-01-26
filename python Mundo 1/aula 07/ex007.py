#desenvolver um programa que leia 2 notas de um aluno e calcular a media 
print("="*30)
print("|     escola de bosta        | ")
print("="*30)
aluno = str(input("Nome do aluno? ")) 
n1 = int(input("diga a 1 nota do aluno {} ".format(aluno)))
n2 = int(input("qual a 2 nota do aluno {} ".format(aluno)))
n3 = int(input("qual a 3 nota do aluno {} ".format(aluno)))
media = (n1+n2+n3)/3
print("Aluno {} tem as notas {:.1f} {:.1f} {:.1f} e tem como media {:.1f}".format(aluno,n1,n2,n3,media))