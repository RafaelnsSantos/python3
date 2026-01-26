#Aprimora o desafio anterior. mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

soma = 0 
valor_maior_2linha = 0
somacoluna = 0
matriz = []
#o c controla a linha
for c in range(3):
    linha = []

    #o J controla a coluna
    for j in range(3):
        valor = int(input(f"Digite um valor [{c+1},{j+1}]: "))
        linha.append(valor)

        if valor %2 == 0:
            soma += valor
        if j == 2:
            somacoluna += valor

    #comparaçao de quem e o maior da 2 linha:        
        if c == 1:
            if valor > valor_maior_2linha:
                valor_maior_2linha = valor

    matriz.append([linha])
#para imprimir a matriz
for linha in matriz:
    for valor in linha:
        print(f"{valor}")
print(f"A soma dos valores pares e {soma}")
print(f"A soma dos valores da terceira coluna e: {somacoluna}")
print(f"O maior valor da segunda linha e: {valor_maior_2linha}")

