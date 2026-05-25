#criar classes capazes de calcular fretes de veiculos
from abc import ABC,abstractmethod
from typing import Any

class trasnporte(ABC):
    def __init__(self,distancia,frete):
        self.distancia = distancia
        self.frete = frete
    @abstractmethod
    def calc_frete(self) -> Any:
        pass

class Moto(trasnporte): #distancia livre
    def __init__(self, distancia, frete = 0,fator=0.50):
        super().__init__(distancia, frete)
        self.fator = fator
        self.distancia = distancia
        self.frete = frete

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f"R${self.frete}"
        
    
class Caminhao(trasnporte): #minino 50km
    def __init__(self, distancia, frete = 0,fator=1.20):
        super().__init__(distancia, frete)
        self.fator = fator
        self.distancia = distancia
        self.frete = frete

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * self.fator
            return f"R${self.frete:.2f}"
        else:
            return "Raio minino de 50km"

class Drone(trasnporte): #maximo 10km
    def __init__(self, distancia = 0, frete = 0,fator=9.50):
        super().__init__(distancia, frete)
        self.fator = fator
        self.distancia = distancia
        self.frete = frete

    def calc_frete(self):
        if self.distancia <= 10:
            self.frete = self.distancia * self.fator
            return f"R${self.frete}"
        else:
            return "Raio minino de 10km"
