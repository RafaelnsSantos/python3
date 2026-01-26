#Criar um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras minusculas 
# maiusculas, quantas letras ao todo sem considerar espaços e quantas letras tem o 1 nome.
nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em: \n Maiusculas:{}".format(nome.lower()))
print("minusculas {}".format(nome.upper()))
print("quantidade de letras: {}".format(len(nome) - nome.count(" ")))
print("Seu 1 nome tem {}".format(nome.find(" ")))

