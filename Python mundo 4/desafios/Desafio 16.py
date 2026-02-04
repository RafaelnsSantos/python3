#crie a classe funcionario, onde tenha os atributos nome, setor e cargo. crie tambem um metodo que permita ao funcionario se apresentar.
from rich import print
class Funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentaçao(self):
        print(f"Ola, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa do curso em Video")
c1 = Funcionario("Maria","Administraçao","Diretora")
c1.apresentaçao()

c2 = Funcionario("Pedro","TI","Programador")
c2.apresentaçao()