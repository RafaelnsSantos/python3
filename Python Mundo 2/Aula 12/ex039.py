#Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade
# se ele ainda vai se alistar ao serviço militar. , se e a hora de se alistar , se ja passou
# do tempo do alistamento , alem o programa deve mostra tempo que falta ou que passou do prazo
from datetime import date
print("-=-"*15)
print("Programa de alistamento militar brasileiro")
print("-=-"*15)

print("[1] se voce for HOMEN \n[2] Para se voce for MULHER.")
escolha = int(input("Digite o numero da opçao:"))
ano = int(input("Ano do Nascimento: "))
nome = str(input("Qual seu nome? "))
atual = date.today().year 
calculo = atual - ano #anos do candidato
previsao = 18 - calculo #estimativa de tempo 
prev = atual + previsao 
anti = calculo - 18
antprev = atual - anti

if escolha == 2:
    print("Infelizmente voce nao pode se alistar")
    print("O alistamento militar e apenas para homens maiores de 18")

elif escolha == 1:
    if calculo == 18:
        print("candidato {} nasceu em {} tem {} em {}".format(nome,ano,calculo,atual))
        print("Voce ja pode se alistar")
    elif calculo < 18:
        print("Candidato {} nasceu em {} tem {} em {}".format(nome,ano,calculo,atual))
        print("Ainda faltam {} anos para seu alistamento ".format(previsao))
        print("Seu alistamento esta previsto para {}".format(prev))
    elif calculo > 18:
        print("Candidato {} nasceu em {} tem {} em {}".format(nome,ano,calculo,atual))
        print("Voce deveria ter se alistado a {} anos atras em {}".format(anti,antprev))
else:
    print("Opçao invalida ")


