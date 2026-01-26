#Cria um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
#lista única que mantenha separados os valores pares a impares. No final. 
#mostre os valores pares e imparas em ordem crescente.
valores = [[],[]]
for c in range (7):
    valor = int(input(f"Digite o {c+1}º valor: "))
    if valor%2 == 0:
        valores[0].append(valor)
        valores[0].sort()

    elif valor%2 == 1:
        valores[1].append(valor)
        valores[1].sort()

print(f"Os valores digitados: {valores} \nValores Pares digitados: {valores[0]} \nValores Impares: {valores[1]}")
