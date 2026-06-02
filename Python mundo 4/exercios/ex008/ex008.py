class ContaBancaria:
    """
    cria uma conta bancaria e permite fazer saques e depositos

    """
    def __init__(self,id,nome,saldo=0):
        self.id = id #Publico (+)
        self._titular = nome #protegido (#)
        self.__saldo = saldo #privado (-)
        print(f"Conta {self.id} criada com sucesso. Saldo atual de {self.__saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de saldo"
    
    def deposito(self,valor):#para metodos e obrigatorio ter self
        valor = abs(valor)
        self.__saldo += valor
        print(f"deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def saque(self,valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.id} : SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")