#o mesmo professor do desafio 19 quer sortear a ordem de apresentaçao de trabalhos dos alunos faça um programa
#que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random
a1 = str(input("Aluno(a) 1: "))
a2 = str(input("Aluno(a) 2: "))
a3 = str(input("Aluno(a) 3: "))
a4 = str(input("Aluno(a) 4: "))
lista = random.sample([a1,a2,a3,a4],k=4)
print("A ordem de apresentaçao E: {}".format(lista))