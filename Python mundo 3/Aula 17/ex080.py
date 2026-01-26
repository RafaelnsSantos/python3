#crie um programa que o user possa digitar cinco valores numericos e cadastre - os em uma lista ,ja na posiçao
#correta de inserçao(sem usar o sort()) no final mostre na lista ordenada na tela

lista = []
for c in range (0,5):
    valores = int(input("Digite um valor: "))
    if len(lista) == 0 or valores > lista [-1]:
        lista.append(valores)
        print("Adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos,valores)
                print(f"Adicionado na posiçao {pos}")
                break
            pos += 1

print(f"Os valores digitados em ordem foi: {lista}")
