#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.faça um programa que ajude ele
#lendo o nome deles e escrevendo o nome do escolhido
import random
a1 = str(input("nome do 1 aluno(a):"))
a2 = str(input("nome do 2 aluno(a):"))
a3 = str(input("nome do 3 aluno(a):"))
a4 = str(input("nome do 4 aluno(a):"))
print("Aluno(a) {} foi sorteado para apagar o quadro".format(random.choice([a1,a2,a3,a4])))