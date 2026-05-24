#Implementar diagrama de classes de poligono(ABC), que vai ter de filhas quadrado e circulo
from abc import ABC,abstractmethod
class poligono(ABC):
    def __init__(self,qtd_lados = 0) -> None:
        self.qtd_lados = qtd_lados
    @abstractmethod
    def Perimetro(self) -> float:
        pass
    @abstractmethod
    def Area(self) -> float:
        pass

class Quadrado(poligono):
    def __init__(self, qtd_lados) -> None:
        super().__init__(qtd_lados)
        self.lado = qtd_lados
    
    def Perimetro(self) -> float:
        perimetro_resultado = self.lado * 4
        return perimetro_resultado

    def Area(self) -> float:
        Area_resultado = self.lado * self.lado
        return Area_resultado

class circulo (poligono):
    def __init__(self, qtd_lados) -> None:
        super().__init__(qtd_lados)
        self.raio = qtd_lados
    
    def Perimetro(self) -> float:
        conta = (2 * 3.14) * self.raio
        return conta

    def Area(self) -> float:
        pi = 3.14
        conta_area = pi * (self.raio**2)
        return conta_area
