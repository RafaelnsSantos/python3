#Crie uma classe Produto, onde podemos cadastrar nome e o preço. crie tambem um metodo que mostre uma etiqueta de preço do produto.
from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço
    def etiqueta(self):
        tam = len(self.nome)
        etiquetaa = Panel(renderable=f"{self.nome}" + "\n" + "-"*tam + "\n" + "."*tam + f"R${self.preço:.2f}" + "."*tam, title="Produto", width=37)
        print(etiquetaa)
p1 = Produto("Iphone 17 Pro Max",25_000.85)
p2 = Produto("Notebook Gamer ",8_000)
p1.etiqueta()
p2.etiqueta()



        