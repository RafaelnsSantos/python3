#isso tudo eo mold
#declaraçao de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que uma pessoa que tem nome e idade

    para criar um nova pessoa use 
    variavel = gafanhoto(nome,idade)
    """
    def __init__(self,nome='vazio',idade=0):#metodo construtor  #self e um nome generico que vai ser atribuido ao nome do objeto que chamou
    #atributos de instancia
        self.nome = nome
        self.idade = idade

    #METODOS DE INSTACIA
    def aniversario(self): 
        self.idade += 1

    def __str__(self): #dunder method
        #quando der print ele vai retorna a mensagem do return mais facil
        return f"{self.nome} e ganfanhoto(a) e tem {self.idade} anos de idade."
    def __getstate__(self):
        return f"estado: = nome= {self.nome} ; idade = {self.idade}"


#declaraçao de objetos
g1 = Gafanhoto(nome="maria",idade=17)
g1.aniversario() 
print(g1)
print(g1.__dict__) # vai mostra em forma de dicionario #e um attribute
print(g1.__getstate__()) # dunder metodo
print(g1.__class__)
print(g1.__doc__)#dunder attribute

#g2 = Gafanhoto(nome='Rafael',idade=17)
#g2.aniversario()
#print(g2)
#print(g2.__getstate__())

#g3 = Gafanhoto()
#print(g3)

#print(g1.__doc__)#dunder attribute

