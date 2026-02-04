#Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,podendo escrever frases na cor relativa. AZUL,VERMELHO E VERDE 
from rich import print
class Caneta:
    def __init__(self,cor):
        self.cor = cor 
        self.destamparr = False
    def destampar(self):
        self.destamparr = True
    def escrever(self,mensagem):
        if self.destamparr == True:
            if self.cor == "azul":
                print(f"[cyan]{mensagem}[/]")
            if self.cor == "vermelha":
                print(f"[red]{mensagem}[/]",end="")
            elif self.cor == "Verde":
                print(f"[green]{mensagem}[/]")
            else:
                print(f"Sua caneta nao tem a cor {self.cor}")
        elif self.destamparr == False:
            print(f"A caneta {self.cor} esta tampada")
    def quebra_linha(self,n):
        for c in range(n):
            print()

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("Verde")
c4 = Caneta("roxo")

c1.destampar()
c2.destampar()
c3.destampar()

c4.destampar()
c1.escrever("ola,tudo bem?")
c1.quebra_linha(0)
c2.escrever("ola,gafanhoto! ")
c3.escrever("Vamos exercitar! ")
c4.escrever("alooo")