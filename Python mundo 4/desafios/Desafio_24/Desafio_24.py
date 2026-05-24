#simular uma cafeteira
from abc import ABC,abstractmethod
class BebidaQuente(ABC):
    def __init__(self) -> None:
        pass
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print("1. Fervendo agua a 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self) -> None:
        super().__init__()

    def misturar(self):
        print(f"2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print(f"3. Servindo em xicara pequena")
        print("--- Bebida Pronta ---")


class Cha(BebidaQuente):
    def __init__(self) -> None:
        super().__init__()

    def misturar(self):
        print(f"2. Mergulhando o sachê de ervas na agua.")

    def servir(self):
        print(f"3. Servindo com canela na caneca de porcelana com limao")
        print("--- Bebida Pronta ---")


class leite(BebidaQuente):
    def __init__(self) -> None:
        super().__init__()

    def misturar(self):
        print(f"2. passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print(f"3. Servindo na caneca grande, ja com cafe.")
        print("--- Bebida Pronta ---")


