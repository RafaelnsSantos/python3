#faça um programa que mostre a tabuada de varios numeros um de cada vez, para cada valor digitado
#pelo user. o programa vai ser interrompido quando o numero solicitado for negativo.
cont = 1
multiplicaçao = 0
while True:
    n = int(input("Digite um valor: "))
    if n < 0:
        break
    for cont in range (1,11):
        multiplicaçao = n * cont
        print(f"{n} x {cont} = {multiplicaçao}")