#Crie uma classe Produto, onde podemos cadastrar nome e o preço. crie tambem um metodo que mostre uma etiqueta de preço do produto.
from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço
    def etiqueta(self):
        conteudo = f"{self.nome.center(30,' ')}"
        conteudo += f"{'-'*30}"
        preçof = f"R${self.preço:,.2f}"
        conteudo += f"{preçof.center(30, '.')}"
        etiquetaa = Panel(conteudo,title="Produto", width=34)
        print(etiquetaa)
p1 = Produto("Iphone 17 Pro Max",25_000.85)
p2 = Produto("Notebook Gamer ",8_000)
p1.etiqueta()
p2.etiqueta()



        