#faça um programa que leia o peso de cinco pessoas no final mostre qual foi o maior peso e o
#menor peso lidos
maior = 0
menor = 0
for c in range (1,6):
    kg = float(input("Qual peso da pessoa N{} ? ".format(c)))
    #atribriu a 1 vez no maior o peso e na menor o peso da 1 pessoa ae depois desenrola 
    #certo com if e else colocando no maior o peso maior e menor no menor 
    if c == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        elif kg < menor:
            menor = kg
print("O maior peso lido {:.1f}Kg\no menor peso lido {:.1f}Kg ".format(maior,menor))
