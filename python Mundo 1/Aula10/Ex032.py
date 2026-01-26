#faça um programa que leia um ano qualquer e mostre se ele e bissexto
print("="*40)
print("|       Programa de ano bissexto       |")
print("="*40)

ano = int(input("Digite um Ano qualquer: "))

if int(ano%4 == 0) and (ano%100 !=0) or ano%400 ==0:
    print("O Ano {} e Bissexto.".format(ano))
else:
    print("O Ano {} nao e Bissexto.".format(ano))
    # dentro da aula ele deu uma  bibilioteca chamda datetime com o parametro date.today que ver
    #o ano da maquina do usuario