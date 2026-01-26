#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario.
#com 15% de aumento
nome = str(input("Nome do colaborador(a): "))
salario = float(input("Salario do colaborador(a):R$ "))

porcentagem = (salario * 15)/100
acrescimo = salario + porcentagem
print("Parabens colaborador(a) {} voce recebeu um aumento de 15% no seu salario, de R${} voce vai passar a receber R${}".format(nome,salario,acrescimo))