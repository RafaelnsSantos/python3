#criar um algoritimo que leia o numero e mostre o dobro, triplo e raiz quadrada do numero
numero = int(input("digite um numero qualquer: "))
dobro = numero * 2
triplo = numero * 3
raizquadrada = numero**(1/2)
print("numero: {} o dobro desse numero e: {} \n o triplo: {} \n raiz quadrada {:2f}.".format(numero,dobro,triplo,raizquadrada))