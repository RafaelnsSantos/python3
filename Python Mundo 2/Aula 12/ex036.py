#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestaçao mensal, sabendo que ela nao pode excender 30% do salario ou entao
#o emprestimo sera negado
print("-=-"*15)
print("|Programa de emprestimo do banco do brasil |")
print("-=-"*15)
#nome = str(input("Digite seu nome: "))
casa = float(input("digite o Valor da casa: R$"))
salario = float(input("Digite o seu salario: R$ "))
finaciamento = int(input("Quantos anos de finaciamento? "))

calculo_finace = casa/(finaciamento*12)
salario_porcento = (salario*30)/100
#print("valor a ser pago R${:.3f} ideal {}" .format(calculo,salario_porcento))
if calculo_finace > salario_porcento:
    print("Para pagar uma casa de R${:.2f} em {} anos a prestaçao sera de R${:.2f}".format(casa,finaciamento,calculo_finace))
    print("Emprestimo Negado!")
else:
    print("Para pagar uma casa de R${:.2f} em {} anos a prestaçao sera de R${:.2f}".format(casa,finaciamento,calculo_finace))
    print("Parabens emprestimo pode ser concedido ")