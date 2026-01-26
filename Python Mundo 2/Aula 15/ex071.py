#crie um programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario qual sera a o valor sacado (inteiro)
#e o programa vai informar quantas cedulas de cada valor serao entregues obs: considere que o caixa possui cedulas de 50,20,10 E 1 reais
print("-=-"*6)
print("|CAIXA ELETRONICO|")
print("-=-"*6)
valor = int(input("qual valor voce quer sacar? "))
total = valor
cedula = 50 
contced= 0
while True:
    if total >= cedula:
        total -= cedula
        contced += 1
    else:
        print(f"Total de {contced} cedulas e de R${cedula}.")
        if cedula == 50:
            cedula  = 20

        elif cedula == 20: 
            cedula = 10

        elif cedula == 10: 
            cedula = 1
        contced = 0
        if total == 0:
            break   