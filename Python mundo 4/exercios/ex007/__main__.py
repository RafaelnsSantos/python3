from rich import inspect,print
from classes import pessoa,aluno,professor,funcionario
def main():
    a1 = aluno(nome="Rafael",idade=18,curso="matematica",turma="13E")
    a1.Fazer_aniversario()
    #inspect(a1,methods=True)
    a1.Fazer_matricula()
    a1.estudar()

    p1 = professor("valdez",35,"Matematica","Mestrado")
    p1.Fazer_aniversario()
    p1.Dar_aula()
    p1.estudar()

    f1 = funcionario("claudia",27,"secretaria","secretaria")
    f1.Fazer_aniversario()
    f1.Bater_ponto()
    f1.estudar()

if __name__ == "__main__":
    main()

