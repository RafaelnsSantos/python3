from abc import ABC,abstractmethod #ABSTRACT BASE CLASSES 

class pessoa(ABC):
    def __init__(self,nome= "",idade= 0):
        self.nome = nome
        self.idade = idade

    def Fazer_aniversario(self):
        self.idade += 1 

    @abstractmethod
    def estudar(self):
        pass


class aluno(pessoa):
    def __init__(self,nome,idade,curso, turma):
        super().__init__(nome,idade) #oque esse super vai fazer ele vai la no init da classe que esta herdado que no caso e a class pessoa e vai executar
        self.curso = curso
        self.turma = turma
    
    def Fazer_matricula(self):
        print (f" o aluno {self.nome} fez a matricula")

    def estudar(self):
        print (f"{self.nome} estuda {self.curso} na turma {self.turma}")


class professor(pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_aula(self):
        print (f"O professor {self.nome} esta dando aula de {self.especialidade} para a sua turma")
    
    def estudar(self):
       print (f"{self.nome} estuda {self.especialidade} para dar aula ")


class funcionario(pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_ponto(self):
        print(f"o(a) funcionario(a) {self.nome} do setor {self.setor} bateu o ponto")

    def estudar(self):
        print(f"{self.nome} se especializa para sua area de {self.cargo}")
