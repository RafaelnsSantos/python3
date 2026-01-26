#Criei um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar 
#quando digitar o valor 999 que e a condiçao de parada no final mostre quantos numeros foram
#digitados e qual foi a soma entre eles

soma = cont = 0
while True:
    n = int(input("Digite um numero qualquer [PARA PARAR DIGITE 999 (STOP)]: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"foram digitados {cont} numeros e a soma dos numeros digitados foi: {soma}")