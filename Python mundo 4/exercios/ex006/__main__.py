from rich import inspect,print
from aluno import aluno
from professor import professor
from funcionario import funcionario

def main():
    a1 = aluno(nome="Rafael",idade=18,curso="Ensino Medio",turma="13E")
    a1.Fazer_aniversario()
    a1.Fazer_matricula()
    #inspect(a1,methods=True)

    p1 = professor("valdez",35,"Matematica","Mestrado")
    p1.Fazer_aniversario()
    p1.Dar_aula()


    f1 = funcionario("claudia",27,"secretaria","secretaria")
    f1.Fazer_aniversario()
    f1.Bater_ponto()
if __name__ == "__main__": #se o nome do arquivo for main ele chama o metodo main , e utilizado para codigos muito grande
    main()

