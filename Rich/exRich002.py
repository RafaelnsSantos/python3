from rich import print
from rich.panel import Panel

caixa = Panel(renderable="Esse aqui e um painel de exemplo",title="Mensagem" ,style="red",width=35)
print(caixa)