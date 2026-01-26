#faça um programa que leia 5 valores numericos e guarde - os em uma lista.
#no final,mostre qual foi o maior e o menor valor e as suas respectivas posiçoes na lista
maior = 0
menor = 0
lista = []
for c in range (0,5):
    lista.append(int(input('Digite um valor: ')))

print(f"os numeros foram: {lista}")
print(f"O maior numero da lista foi: {max(lista)} nas posiçoes:", end = ' ' )

maior = max(lista)
menor = min(lista)
for v ,c in enumerate(lista):
    if c == maior:
        print(f'{v}..',end = ' ')
print()
print(f"E o menor valor foi {min(lista)} nas posiçoes : ",end = ' ')
for v ,c in enumerate(lista):
    if c == menor:
        print(f'{v}..',end = ' ')
print()

