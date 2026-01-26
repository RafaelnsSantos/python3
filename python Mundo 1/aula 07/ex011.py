#faça um programa que leia a largura e a altura de uma parede em metros calcule sua area 
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta
#uma area de 2m^2.
altura = float(input("qual a altura da parede? "))
largura = float(input("qual a largura da parede? "))

calculo1 = altura * largura 
calculo2 = calculo1 / 2

print("Voce vai precisar cerca de {:.0f} litros de tinta ".format(calculo2))