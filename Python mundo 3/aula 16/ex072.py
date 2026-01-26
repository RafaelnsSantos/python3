#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero ate vinte ,seu programa vai ler um numero pelo teclado (ente 0 e 20) e mostra-lo por extenso.
n = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    while True:
        n_teclado = int(input("Digite um numero de 0 a 20: "))
        if 0 <= n_teclado <= 20:
            break 
    print (f"Voce digitou o numero {n[n_teclado]}")
    escolha_user = str(input("Voce quer continuar? [S/N]: ")).strip().upper()[0]

    if escolha_user != 'S':
        break