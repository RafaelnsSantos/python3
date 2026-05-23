from pessoa import pessoa
class funcionario(pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def Bater_ponto(self):
        print(f"o(a) funcionario(a) {self.nome} do setor {self.setor} bateu o ponto")