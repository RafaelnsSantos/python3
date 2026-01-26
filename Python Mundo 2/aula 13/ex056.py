#desenvolva o programa que leia o nome idade sexo de 4 pessoas no final o programa deve mostra:
#a media de idade do grupo, qual o nome e idade do HOMEm mais velho , e quantas mulheres tem menos de 20
#anos.
media = 0
idadeH = 0
nomeh = 'a'
totM = 0
for c in range (1,5):
    print("---- {} Pessoa ----".format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("M/F: ")).strip().lower()

    media += (idade)/4
    if (sexo in 'Mm') and (idade > idadeH):
        idadeH = idade 
        nomeh = nome
    elif (sexo in 'Ff') and (idade < 20):
        totM += 1

print('A media do grupo e {}\nO homen mais velho tem {} e se chama {}\nao todo sao {} mulheres com menos de 20 anos '.format(media,idadeH,nomeh,totM))