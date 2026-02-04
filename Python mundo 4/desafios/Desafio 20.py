#Crie uma classe chamada gamer, onde podemos cadastrar nome,nick e jogos favoritos de uma pessoa. Crie tambem
#um metodo que permita mostra a ficha desse gamer 
from rich import print
from rich.panel import Panel
class gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    def add_favoritos(self,jogo):
        self.jogos.append(jogo)
    def ficha(self):
        jogos_str = "\n".join(sorted(self.jogos))
        ficha = Panel(renderable=f"Nome Real: [bold cyan]{self.nome}[/]\nJogos favoritos:\n[blue]{jogos_str}[/]", title=f"Jogador(a) <{self.nick}>", width=65)
        print(ficha)
j1 = gamer("Rafael Nascimento","Rafayauh")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()
