#faça um programa que leia um numero inteiro e diga se ele e ou nao numero primo
n = int(input("Digite um numero: "))
tot = 0
for c in range (1,n +1):
    if (n%c == 0):
        tot += 1
    print("{}".format(c),end=" ")
print("\no numero {} foi divisivel {} vezes ".format(n,tot))
if tot == 2:
    print("E por isso ele e um numero PRIMO!")
else:
    print("por isso ele NAO e primo")