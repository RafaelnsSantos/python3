#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' OU 'F'. caso esteja errado
#peça para digitar novamente ate ter o valor correto.
sexo = ''
c = 0
while sexo not in ('m','f'):
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().lower()[0] 

    if sexo not in ('m', 'f'):
         print("Digite um sexo valido!")