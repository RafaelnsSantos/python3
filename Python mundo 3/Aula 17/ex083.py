#crie um programa onde o usuario digite um expressao qualquer que use parenteses .Seu aplicativo devera analisar
#se a expressao passada esta com os parenteses abertos e fechados na ordem correta.
lista = []
expressao = str(input("Digite uma expressao: "))
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("sua Expressao esta certa.")
else:
    print("sua expressao esta errada.")
