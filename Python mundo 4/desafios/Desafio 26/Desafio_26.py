#Estrutura para calcular salarios de funcionarios
from rich.panel import Panel
from rich import print
from abc import ABC,abstractmethod
class Funcionario(ABC):
    def __init__(self,nome,sal_bruto,salario,sal_min =1612,inss=7.5) -> None:
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def calc_sal(self):
        pass
    
    def analisar_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self, nome, valor_hora,horas_trab,sal_bruto=0, salario=0, sal_min=1612, inss=7.5) -> None:
        super().__init__(nome, sal_bruto, salario, sal_min, inss)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        desconto_inss = (self.sal_bruto/100) * self.inss
        self.salario = self.sal_bruto - desconto_inss

    def analisar_sal(self):
        painel_analise = Panel(f"O salario de {self.nome} (Funcionario Horista) e de {self.salario:.2f} e corresponde a {self.salario/self.sal_min:.1f} salarios mininos", title="Analise de salario", width=50)
        print(painel_analise)

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario=0, sal_min=1612, inss=7.5) -> None:
        super().__init__(nome, sal_bruto, salario, sal_min, inss)

    def calc_sal(self):
        desconto_inss = (self.sal_bruto/100)*self.inss
        self.salario = self.sal_bruto - desconto_inss

    def analisar_sal(self):
        painel_analise = Panel(f"O salario de {self.nome} (Funcionario Horista) e de {self.salario:.2f} e corresponde a {self.salario/self.sal_min:.1f} salarios mininos", title="Analise de salario", width=50)
        print(painel_analise)

