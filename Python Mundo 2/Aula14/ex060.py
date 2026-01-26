#faca um programa que leia um numero qualquer e mostre o seu fatorial ex: 5! 
# 5x4x3x2x1 = 120
n = int(input("Digite um numero: "))
c = n +1
mult = 1
print("calculando: {}! = ".format(n),end = '')
while c > 1:
    c -= 1
    mult *= c
    print(" {} ".format(c),end = '')
    print("x" if c > 1 else '= ', end = '')
print("{}".format(mult),end = '')

#fazer com o for =
