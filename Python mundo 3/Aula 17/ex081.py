#crie um programa que vai ler varios numeros e colocar em uma lista depois disso mostre:
#A) quantos numeros foram digitados. B) A lista de valores ordenada de forma decrescente. c)Se o valor 5 foi
#digitado e esta ou nao na lista.
lista = []
cont5 = 0
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    cont += 1
    lista.append(valor)
    lista.sort(reverse = True)
    #
    escolha_user =  ' '
    while escolha_user != 'SN':
        escolha_user = str(input("Quer continuar? [S/N]: ")).strip().upper()
        if escolha_user in'SN':
            break

    if escolha_user == 'N':
        break

print(f"Voce digitou {cont} elementos")
print(f"Os valores em ordem decrescente sao: {lista} ")

if 5 in lista:
    print("o numero 5 faz parte da lista. ")
    cont5+= 1
elif 5 not in lista:
    print("O numero 5 nao faz parte da lista. ")