#criei um progrma que leia dos valores e mostre um menu na tela [1] somar , [2] multiplicar
#[3] maior ,[4] novos numeros [5] sair do programa seu programa devera realizar a operaçao
#solicitada em cada caso
n1 = float(input("Digite um valor: "))
n2 = float(input("digite outro valor: "))
maior = n1 
escolha_user = 0
while escolha_user != 5:
    print("---------MENU---------")
    print("[1] SOMA \n[2]MULTIPLICAR\n[3] MAIOR \n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA")
    escolha_user = int(input("Sua opçao: "))
    if escolha_user == 1:
        soma = n1+n2
        print("A soma dos numeros: {} + {} = {} ".format(n1,n2,soma))
    elif escolha_user == 2:
        mult = n1*n2
        print("A multiplicaçao dos numeros: {} * {} = {}".format(n1,n2,mult))
    elif escolha_user == 3:
        if n1 > n2:
            maior = n1
            print("O maior numero entre {} e {} foi o {} ".format(n1,n2,maior))
        else:
            maior = n2
            print("O maior numero entre {} e {} foi o {} ".format(n1,n2,maior))
    elif escolha_user == 4: 
        n1 = float(input("Digite um novo valor: "))
        n2 = float(input("digite um outro novo valor: "))
    elif escolha_user > 5:
        print("voce digitou um numero invalido")