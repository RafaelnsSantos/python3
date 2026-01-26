#faça um programa que calcule a soma entre todos os numeros impares que sao multiplo de tres
#e que se encontram no intervalo de 1 ate 500
s = 0
c1 = 0
for c in range(3,500,6):
    c1 += 1
    s += c
print("A soma de todos os {} valores e {}".format(c1,s))