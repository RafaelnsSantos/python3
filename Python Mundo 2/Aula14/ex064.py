#crie um programa que leia varios numeros inteiros pelo teclado. o programa so vai para quando
#user digitar 999. que e a condiçao de parada. no final mostre quantos numeros foram digitados
#e qual foi a soma entre eles , desconsiderando o {999}
#exemplo caro de acumulador e contador
cont = 0
n = 0 
soma = 0
while n < 999:
    n = int(input(("digite um numero qualquer [999 para PARAR (STOP)]: ")))
    if n < 999:
        cont += 1
        soma += n
print("Numeros digitados: {} \na soma dos numero digitados:{}".format(cont,soma))