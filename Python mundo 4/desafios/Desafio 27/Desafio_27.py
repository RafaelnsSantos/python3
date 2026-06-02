#simular sistema de batalha entre personagem de um rpg
from abc import abstractmethod,ABC
import random

class Personagem(ABC):
    def __init__(self,nome,vida) -> None:
        self.nome = nome
        self.vida = vida    
        self.golpes = []

    def atacar(self,alvo,forca = 50):
        if self.Vivo_morto() > 0 and alvo.vida > 0:
            dano = self.receber_dano (forca=forca)
            golpe_ramdomizado = self.golpes[random.randrange(0,len(self.golpes))]
            print(f"{self.nome} atacou {alvo.nome}, com um golpe {golpe_ramdomizado} de força {forca}\n{alvo.nome} recebeu {dano} de dano")

    def receber_dano(self,dano=0,forca=0):
        dano = random.randint(1,forca)
        return dano
    
    def Vivo_morto(self):
        return int(self.vida)

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Golpe de machado","soco","Pulo giratorio"]

    def curar(self):
        cura = random.randint(1,1000)
        print (f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {cura} pontos de vida")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes=["Bola de fogo","raio de luz","magia Estatica"]

    def curar(self):
        cura = random.randint(1,1000)
        print (f"{self.nome} fez uma magia de cura e recuperou {cura} pontos de vida")
    