#Escrava um programa que pargunte o salário de um Funcionário e calcule o valor do Seu aumento.
#Para salários superiores a R$1.250.00, calcula um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
print("="*40)
print("|  Programa de Aumento de salario   |")
print("="*40)
nome = str(input("Nome do colaborador(A): "))
salario = float(input("Digite o seu Salario: R$ "))
if salario > 1250:
    calculo = (salario*10)/100
    aumento = salario + calculo
    print("Parabens Colaborador(a) {} Voce vai passar de R${} para R${} ".format(nome,salario,aumento))
else:
    calculo = (salario*15)/100
    aumento = salario + calculo
    print("Parabens Colaborador(a) {} Voce Vai passar de R${} para R${}".format(nome,salario,aumento))