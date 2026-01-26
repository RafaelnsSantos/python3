#crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-os (com idade) em um dicionário. se por acaso a CTPS for diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. calcule e acrescente, além
# da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
aposentadoria = {}

for c in range (1):
    anoatual = date.today().year
    nome = str(input("Nome: ")).strip()
    anonascimento = int(input("Data de nasciemnto: "))
    idade = anoatual - anonascimento
    carteira_trabalho = int(input("Carteira de trabalho: (0 Nao tem): "))

    aposentadoria['nome'] = nome
    aposentadoria['idade'] = idade
    aposentadoria['ctps'] = carteira_trabalho

    if carteira_trabalho == 0:
        break
    contrataçao = int(input("Ano de contrataçao: "))
    salario = float(input("Salario: R$"))


    aposentadoria['contrataçao'] = contrataçao
    aposentadoria['salario'] = salario
    #calculo da aposentadoria = idade + (35 - (anoatual - contrataçao))
    aposentadoria['aposentadoria'] = (contrataçao + 35) - anonascimento

print("-=-"*5)
for k , c in aposentadoria.items():
    print(f"{k} = {c}")
