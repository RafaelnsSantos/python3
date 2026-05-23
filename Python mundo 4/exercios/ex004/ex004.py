from rich import inspect,print
class pessoa:
    def __init__(self,nome= "",idade= 0):
        self.nome = nome
        self.idade = idade

    def Fazer_aniversario(self):
        self.idade += 1 


class aluno(pessoa):
    def __init__(self,nome,idade,curso, turma):
        super().__init__(nome,idade) #oque esse super vai fazer ele vai la no init da classe que esta herdado que no caso e a class pessoa e vai executar
        self.curso = curso
        self.turma = turma
    
    def Fazer_matricula(self):
        print (f" o aluno{self.nome} fez a matricula")


class professor(pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_aula(self):
        print (f"O professor {self.nome} esta dando aula de {self.especialidade} para a sua turma")


class funcionario(pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_ponto(self):
        print(f"o(a) funcionario(a) {self.nome} do setor {self.setor} bateu o ponto")


a1 = aluno(nome="Rafael",idade=18,curso="Ensino Medio",turma="13E")
a1.Fazer_aniversario()
inspect(a1,methods=True)
a1.Fazer_matricula()

p1 = professor("valdez",35,"Matematica","Mestrado")

##f1 = funcionario()

