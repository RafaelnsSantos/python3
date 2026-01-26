#Crie um programa que leia uma frase qualquer e diga se ela e um polindroma,desconsiderando os espaços.
frase = str(input("digite uma frase: ")).upper().strip().replace(" ","")
inverso = frase[::-1]
print("O inverso de {} e {}".format(frase,inverso))
if frase == inverso:
    print("E um palindromo!")
else:
    print("Nao e um palindromo!")


