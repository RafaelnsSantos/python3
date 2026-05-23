from rich import inspect,print
from classesex005 import aluno,professor,funcionario

a1 = aluno(nome="Rafael",idade=18,curso="Ensino Medio",turma="13E")
a1.Fazer_aniversario()
inspect(a1,methods=True)
a1.Fazer_matricula()

p1 = professor("valdez",35,"Matematica","Mestrado")

##f1 = funcionario()

