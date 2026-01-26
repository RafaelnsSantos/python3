#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#  sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

carro = int(input("Quantos dias voce alugou o carro?: "))
km_rodado = float(input("Quantos km voce percorreu? "))

conta = (60*carro)+(km_rodado*0.15)

print("Voce ficou com o carro por {} dias \n percorreu {}km \n o preço a ser pago pelo uso e de {}".format(carro,km_rodado,conta))