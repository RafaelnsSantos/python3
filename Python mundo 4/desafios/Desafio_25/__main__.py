from Desafio_25 import *

def main():
    dist = 10
    entrega = Drone(dist)

    print(f"Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}")

if __name__ == "__main__":
    main()