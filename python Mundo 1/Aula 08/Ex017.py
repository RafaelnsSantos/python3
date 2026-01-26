#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa.
ca = float(input("Valor do cateto oposto: "))
co = float(input("valor do cateto adjacente: "))
h2 = (ca**2)+(co**2)
h = h2**(1/2)
print("Seu cateto oposto:{} \n cateto adjacente: {} \n tem como hipotenusa {:.2f} ".format(ca,co,h))