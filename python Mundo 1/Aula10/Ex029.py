#Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80km/h, mostre uma 
#mensagem dizendo que ele foi multado. A multa vai cusa R$7,00 Por cada km acima do limite
print("="*38)
print("|Programa de multa do governo federal|")
print("="*38)
velocidade = float(input("Quantos Km/h seu veiculo estava?  "))

if velocidade > 80:
    calculo = (velocidade - 80) * 7
    print("Voce Ultrapassou o limite de 80km/h")
    print("Voce vai precisar paga a multa de R${:.0f}".format(calculo))
else:
    print("Muito bem ande nos limites da lei ")