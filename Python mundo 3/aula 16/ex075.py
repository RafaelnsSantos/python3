#Desenvolva um programa que leia quatro valores pelo teclado a guarda-os em uma tupla. No final. mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os numeros pares.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite mais outro valor: "))
n4 = int(input("Digite ultimo valor: "))
cont9 = 0
tupla = n1,n2,n3,n4
print(f"voce digitou os valores:{tupla}")

#USA COUNT NAO FOR PARA CONTA NA TUPLA KKKKKKKK
print(f"O valor 9 apareceu {tupla.count(9)} vezes")

#da pra somar +1 no index
if 3 in tupla:
    print(f"o valor 3 foi encontado na {tupla.index(3)+1} posiçao")
else:
    print("O 3 nao foi encontrado em nenhuma posiçao")

print("Os valores pares digitados foram:",end = ' ')
for c in tupla:
    if c % 2 == 0:
        print(c,end= " ")

