#Faça um programa que leia tres numero e mostre qual e o maior e qual e o menor.
n1 = float(input("Digite o 1 numero: "))
n2 = float(input("Digite o 2 numero: "))
n3 = float(input("Digite o 3 numero: "))

maior = n1
menor = n1

if (n1 > n2 and n1>n3):
    maior = n1  
if n2 > maior:
    maior = n2 
if n3 > maior:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < menor: 
    menor = n2
if n3 < menor:
    menor = n3

print("O maior valor {:.0f} \n menor valor {:.0f}".format(maior,menor))


