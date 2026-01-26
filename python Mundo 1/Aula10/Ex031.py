#Desenvolva um programa que pergunte a distancia de uma viagem em km Calcule o preço da passagem, cobrando
#R$0.50 por km para viagem de ate 200km e R$0,45 para viagem mais longa
print("="*50)
print("|Programa de tarifas rodovirias do governo federal|")
print("="*50)
distancia = float(input("Qual a distancia da viagem em km? "))
if distancia <= 200:
    calculo = distancia * 0.50 
    print("Voce vai precisar pagar R${:.1f} para essa viagem de {:.0f}Km/h".format(calculo,distancia))
else:
    calculo = distancia  * 0.45
    print("Voce vai precisar pagar R${:.1f} para essa viagem de {:.0f}Km/h".format(calculo,distancia))