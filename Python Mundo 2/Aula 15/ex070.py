#Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar
#no final mostre total gasto na compra b)quantos produtos custam mais de mil reais , c)qual e o nome do produto mais barato.
print("-=-"*5)
print("|LOJA DA BARATA|")
print("-=-"*5)
soma_produto = 0
produto_barato = ''
cont_produto_caro = 0 
cont = 0
preço_menor = 0
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$ "))
    cont += 1
    soma_produto += preço

    if preço > 1000:
        cont_produto_caro += 1
    
    if cont == 1:
        produto_barato = produto
        preço_menor = preço

    if preço < preço_menor:
        produto_barato = produto
        preço_menor = preço

    escolha_user = ' '
    while escolha_user not in 'SN':
        escolha_user = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if escolha_user == 'N':
        break

print(f"O total da compra foi R${soma_produto} \nTemos {cont_produto_caro} produtos custando mais que mil reias \nO produto barato foi {produto_barato} custando R${preço_menor}")