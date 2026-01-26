#Desenvolva um programa que leia seis numeros inteiro e mostre a soma apenas daqueles que forem pares 
#se o valor digitado dor impar desconsidere-o
#contador e acumulaor 
soma = 0 
cont = 0
for c in range (1,7):
    n = int(input("digite um numero:"))
    if n%2 == 0:
        cont += 1
        soma += n    
print("Voce informou {} numero pares e a soma foi : {}".format(cont,soma))