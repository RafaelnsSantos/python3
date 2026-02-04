#esse install mostra de uma forma mais clara o erro 
from rich.traceback import install
install()

def divisao(x,y):
    return x /y

print(divisao(50,0))