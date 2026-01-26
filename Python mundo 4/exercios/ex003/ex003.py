class ContaBancaria:
    """
    cria uma conta bancaria e permite fazer saques e depositos

    """
    def __init__(self,id,nome,saldo=0):
        self.id = id 
        self. nometitular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de {self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.nometitular} tem R${self.saldo:,.2f} de saldo"
    
    def deposito(self,valor):#para metodos e obrigatorio ter self
        self.saldo += valor
        print(f"deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def saque(self,valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.id} : SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")

c1 = ContaBancaria(id=112,nome="Rafael Nascimento",saldo=3000)
c1.deposito(500)
c1.saque(1000)
print(c1)