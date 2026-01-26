#Elabora um programa que calcule o valor a ser pago por um produto. 
#considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
print("-=-"*5)
print("|LOJA DO RAFAEL|")
print("-=-"*5)
valor = float(input("Digite o valor do(s) produto(s): R$"))
print("[1] para pagar vista dinheiro ou cheque \n[2] para pagar no cartão")
formapag = int(input("Digite o numero: "))
vista = (valor*10)/100
vista1 = valor - vista
vista_cartao = (valor*5)/100
vista_cartao1 = valor - vista_cartao
vista3 = valor*1.20
if formapag == 1:
    print("Voce vai pagar R${} pelo(s) produto(s)".format(vista1))
elif formapag == 2:
    print("[1] a vista no cartao \n[2] Pagar em 2x no cartao \n[3] Paga em 3x ou mais no cartao")
    formapag2 = int(input("digite o numero: "))

    if formapag2 == 1:
        print("Voce vai pagar R${} pelo(s) produto(s)".format(vista_cartao1))
    elif formapag2 == 2:
        print("Voce vai pagar R${} pelo(s) produto(s)".format(valor))
    elif formapag2 == 3:
        vezes = int(input("Quantas parcelas? "))
        vista2 = vista3/vezes
        print("Sua compra sera parcelada em {}X de {} com JUROS de 20%".format(vezes,vista2))
        print("Voce vai pagar R${} pelo(s) produto(s)".format(vista3))