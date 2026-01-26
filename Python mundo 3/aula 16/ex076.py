#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia
#no final mostre uma listagem de preços organizando os dados em forma tabular

#o nome dos produtos e par e o numero e impar entao no caso 0 par 1 impar e por ae vai 
produtos = ("Arroz", 10,
"Feijão", 8,
"Macarrão", 12,
"Leite", 6,
"Ovos", 9,
"Pão", 5,
"Queijo", 15,
"Carne", 20,
"Tomate", 7,
"Cebola", 4)

print("---"*20)
print(f"| {'listamgem de preço':^56} |")
print("---"*20)
for c in range (0,len(produtos)):
    if c % 2 ==0 :
        print(f"{produtos[c]:.<30}",end = '')
    else:
        print(f"R${produtos[c]:>5.2f}")
print("---"*20)
