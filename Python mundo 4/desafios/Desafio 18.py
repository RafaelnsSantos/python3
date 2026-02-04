#Crie uma classe churrasco, onde seja possivel informar quantas pessoas vao participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# consumo por pessoa : 400g
#preço: R$82,40/kg
from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self,titulo,quant_pessoas):
        self.titulo = titulo
        self.quant_pessoas = quant_pessoas
    def analisar(self):
        recomendaçao_compra = (self.quant_pessoas * 400) / 1000
        custo_total = recomendaçao_compra * 82.40
        custo_por_pessoa = custo_total/self.quant_pessoas

        analise = Panel(renderable=f"Analizando [green]{self.titulo}[/] com [bold blue]{self.quant_pessoas}[/] convidados\nCada participante comera 400g e cada kg custa R$82.40\nRecomendado comprar [bold blue]{recomendaçao_compra}[/]KG de carne O custo total sera de [green]R${custo_total:.2f}[/]\nCada pessoa pagara [yellow]R${custo_por_pessoa}[/] para participar.", title=f"{self.titulo}", width=65)
        print(analise)
c1 = Churrasco("Churras dos amigos",15)
c1.analisar()