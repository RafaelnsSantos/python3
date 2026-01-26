#Cria um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No Final, mostre a matriz na tela com a Formataçao correta.

#matriz 
matriz = []
for c in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor [{c},{j}]: "))
        linha.append(valor)
    matriz.append([linha])

for linha in matriz:
    for valor in linha:
        print(f"{valor}")

