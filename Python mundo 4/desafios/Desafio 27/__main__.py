from Desafio_27 import *

def main():
    p1 = Guerreiro(nome="Kratos",vida=2000,golpes="furacao")
    p2 = Mago(nome="Merlin",vida=3000,golpes="furacao")

    p1.atacar(p2,forca=2000)
    p2.curar()
    p2.atacar(p1,forca=5000)
    p2.curar()

if __name__=="__main__":
    main()