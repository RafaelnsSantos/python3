class Availacao():
    def __init__(self,nome,disciplina,nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota
#metodos acessores
    def get_nota(self): #motodo getter
        return self._nota 

    def set_notas(self,valor): #metodo Settter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("nota invalida") 