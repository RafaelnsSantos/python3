from ex008 import *


def main():
    c1 = ContaBancaria(id=111,nome="maria",saldo=3000)
    c1.saque(1000)
    c1._titular = "pedro"
    print(c1)
if __name__ =="__main__":
    main()