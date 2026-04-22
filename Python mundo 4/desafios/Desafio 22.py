#Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal,volume,ligar/desligar)
from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int =1
    volume_max:int =5

    def __init__(self, canal = 1,volume=2):
        self.ligado:bool = False
        self.volume_atual:int = volume
        self.canal_atual:int = canal
    
    def liga_desliga(self):
        self.ligado = not self.ligado
    
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
        else:
            self.canal_atual -= 1 

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostra_tv (self):

        conteudo = ''
        if not self.ligado:
            conteudo = f"[red]A TV esta desligada[/red]"
        else:
            conteudo = f"CANAL = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/] "
                else:
                    conteudo += f"{canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min,ControleRemoto.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"

        tv = Panel(conteudo, title="[TV]",width=30)
        print(tv)
        
tv = ControleRemoto(2,1)
while True:
    tv.mostra_tv()
    comando = str(input(f"<CH{tv.canal_atual}> - VOL{tv.volume_atual} + "))
    match comando:
        case "0":
            break
        case "@":
            tv.liga_desliga()
        case ">":
            tv.canal_mais()
        case "<":
            tv.canal_menos()
        case "+":
            tv.volume_mais()
        case "-":
            tv.volume_menos()
    print("\n" * 10)