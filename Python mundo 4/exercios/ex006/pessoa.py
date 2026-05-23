class pessoa:
    def __init__(self,nome= "",idade= 0):
        self.nome = nome
        self.idade = idade

    def Fazer_aniversario(self):
        self.idade += 1 