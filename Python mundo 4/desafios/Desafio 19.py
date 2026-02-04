#Crie a classe livro que vai simular a passagem de paginas de um livro considerando tambem se o usuario chegou ao fim da leitura
from rich import print
class livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.paginas_total = paginas
        self.pagina = 1
        print(f"Voce acabou de abrir o livro '{self.titulo}'que tem {self.paginas_total} no total. voce agora esta na pagina {self.pagina}")

    def avançar_paginas(self,pagina):
        cont = 1
        if self.pagina >= self.paginas_total:
            print(f"[yellow]Você já terminou o livro '{self.titulo}'![/]")
            return
        for c in range(pagina) :
            if self.pagina < self.paginas_total:
                self.pagina += 1
                cont += 1
                print(f"pag{self.pagina} -> ",end='')
        print(f"[blue]Voce avancou {cont-1} paginas e agora esta na pagina {self.pagina}[/]")
        if self.pagina == self.paginas_total:
            print(f'[red]Voce chegou ao final do livro "{self.titulo}"[/]')
            return
l1 = livro("10 coisas que aprendi",20)
l1.avançar_paginas(5)
l1.avançar_paginas(10)
l1.avançar_paginas(100)
