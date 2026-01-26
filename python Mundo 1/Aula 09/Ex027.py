#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#para qualquer tamanho 
nome = str(input("digite seu nome completo: ")).strip()
lista = nome.split()
print("primeiro nome: {} ".format(lista[0]))
print("Ultimo sobrenome:{} ".format(lista[-1]))
