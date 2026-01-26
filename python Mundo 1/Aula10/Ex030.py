#Criei um programa que leia um numero inteiro e mostre na tela se ele e Par ou impar.
print("="*30)
print("|          Par ou Impar      |")
print("="*30)

n = int(input("digite um valor qualquer: "))
divisao =  n%2 
if divisao == 0:
    print("O numero {} Ele e Par.".format(n))
else:
    print("O numero {} ele e Impar.".format(n))