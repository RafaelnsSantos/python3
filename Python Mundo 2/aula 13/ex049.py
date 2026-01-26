#refaça o desafio 009,mostrado a tabuada de um numero que o usuario escolheu, so que agora
#utilizado o laço for.
print("-=--"*4)
print("|TABUADA 2.0  |")
print("-=--"*4)

i = int(input("Escolha um numero: "))
for c in range(1,11):
    mult = i * c
    print("{} x {} = {}".format(i,c,mult))

