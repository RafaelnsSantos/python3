#crie um programa que tenha uma funçao chamada leiaint(), que vai funcionar de forma semelhante a 
# funçao input() do python, só que fazendo a validaçao para aceitar apenas um valor numérico inteiro.
#ex: n = leiaint('Digite um n: ')
def leiaint(n=''):
    while True:
        valor = input(n)
        resultado = valor
        r = resultado.isdigit()
        if r == False:
            print("ERRO! digite um numero inteiro valido.")
        else:
            return valor


#progrma principal
n = leiaint('digite um numero: ')
print(f'Voce acabou de digitar o Numero {n}')
