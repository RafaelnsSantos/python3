from pessoa import pessoa
class professor(pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def Dar_aula(self):
        print (f"O professor {self.nome} esta dando aula de {self.especialidade} para a sua turma")