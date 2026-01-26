#isso tudo eo mold
#declaraçao de classe
class Gafanhoto:
    def __init__(self):#metodo construtor  #self e um nome generico que vai ser atribuido ao nome do objeto que chamou
    #atributos de instancia
        self.nome = ''
        self.idade = 0

    #METODOS DE INSTACIA
    def aniversario(self): # esse metodo vai mecher no aniversario 
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} e ganfanhoto(a) e tem {self.idade} anos de idade."

#class eu posso jogar em outro local e chamar pra esse local usando modurizaçao

#aqui vai instaciar
#declaraçao de objetos
g1 = Gafanhoto()#menos esse que o metodo da classe
g1.nome = 'Maria'
g1.idade = 17 #atributos voce so vai atribuir e nada mais
g1.aniversario() #metodo tem parentese para ser chamado ao def construtor 
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Rafael'
g2.idade = 17
g2.aniversario()
print(g2.mensagem())