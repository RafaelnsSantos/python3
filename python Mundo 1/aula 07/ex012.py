#faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
nome = str(input("Nome do produto: "))
produto_n = float(input("Digite o valor do produto:R$ "))

calculo1 = (produto_n * 5)/100
calculo2 =  produto_n - calculo1
print("o produto {} com valor de R${} na liquidaçao tem desconto de 5% e sair por R${} ".format(nome,produto_n,calculo2))
