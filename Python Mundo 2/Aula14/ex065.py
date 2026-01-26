#crie um programa que leia varios numeros inteiros pelo teclado. no final da execuçao, mostre
# a media entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve 
#perguntar ao user se ele quer ou nao continuar a digitar valores
n = 0 
media = 0 
cont = 0
maior = 0
menor = 0
soma = 0
escolha_user = 'S'
while escolha_user != 'N':
    n = int(input("Digite um numero inteiro qualquer: "))
    cont += 1
    escolha_user = str(input("quer continuar?[S/N] ")).strip().upper()[0]
    soma += n
    # maior e menor eu so atribui algo quando ocorreu de cont se == 1 sendo assim maior e  menor
    # quando o cont for igual a 1 ele vao ser o 1 numero podendo se desenrola no codigo depois para
    # a diferenciaçao de menor e maior 
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

media = soma / cont
print("voce digitou {} e a Media foi : {} \nmaior: {} e o menor {} ".format(cont,media,maior,menor))

