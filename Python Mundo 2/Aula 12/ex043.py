#Desenvolva uma lógica que leia o paso a a altura de uma pessoa, 
#calcule seu IMC a mostre seu status, de acordo com a tabala abaixo:
#Abaixo de 18.5: Abaixo do Paso
#Entre 18.5 e 25: Paso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

print("-=-"*6)
print("| CALCULADORA IMC |")
print("-=-"*6)
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso/(altura*altura)
if imc < 18.5:
    print("Voce esta Classificado como MAGREZA ")
elif imc < 25 :
    print("Voce esta Classificado como peso NORMAL")
elif imc < 30:
    print("Voce esta Classificado como SOBREPESO")
elif imc < 40:
    print("Voce esta Classificado como OBESIDADE")
else:
    print("Voce esta Classificado como OBESIDADE MORBIDA.")
print("Voce tem o imc de: {:.1f}".format(imc))