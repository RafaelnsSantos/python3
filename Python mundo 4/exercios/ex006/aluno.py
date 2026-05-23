from pessoa import pessoa
class aluno(pessoa):
    def __init__(self,nome,idade,curso, turma):
        super().__init__(nome,idade) #oque esse super vai fazer ele vai la no init da classe que esta herdado que no caso e a class pessoa e vai executar
        self.curso = curso
        self.turma = turma
        
    def Fazer_matricula(self):
        print (f" o aluno {self.nome} fez a matricula")