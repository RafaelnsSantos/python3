#simular sistema de batalha entre personagem de um rpg
from abc import abstractmethod,ABC
from random import randint,choice

class Personagem(ABC):
    def __init__(self,nome,vida,golpes = ["Golpe de machado","Bola de fogo","soco","Pulo giratorio"]) -> None:
        self.nome = nome
        self.vida = vida    
        self.golpes = golpes

    def atacar(self,alvo,forca):
        dano = self.receber_dano(forca=forca)
        golpe_ramdomizado = choice([self.golpes])
        print(f"{self.nome} atacou {alvo.nome}, com um golpe {golpe_ramdomizado} de força {forca}\n{alvo.nome} recebeu {dano} de dano")

    def receber_dano(self,dano=0,forca=0):
        dano = randint(1,forca)
        return dano

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida, golpes) -> None:
        super().__init__(nome, vida, golpes)

    def curar(self):
        cura = randint(1,1000)
        print (f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {cura} pontos de vida")

class Mago(Personagem):
    def __init__(self, nome, vida, golpes) -> None:
        super().__init__(nome, vida, golpes)

    def curar(self):
        cura = randint(1,1000)
        print (f"{self.nome} fez uma magia de cura e recuperou {cura} pontos de vida")
    