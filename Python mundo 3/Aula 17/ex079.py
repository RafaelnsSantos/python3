#crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
#caso o numero ja exista la dentro ele nao sera adicionado. no final serao exibidos todos os valores unicos
#digitados em ordem crescente.
lista = []
while True:
    valor = int(input("Digite um valor: "))
    
    if valor not in lista:
        lista.append(valor)
        lista.sort()
        print("Valor adicionado a lista")
        
    elif valor in lista:
        print("Valor duplicado! nao vou adiciona a lista")

    #while para repetir pergunta:
    escolha_user = ' '
    while escolha_user != 'SN':
        escolha_user = str(input("Quer continuar: [S/N]: ")).strip().upper()[0]
        if escolha_user in 'SN':
            break

    if escolha_user == 'N': 
        break
print(f"Voce digitou os valores {lista}")