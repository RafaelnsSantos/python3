#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um de seus digitos separados
#unidade,dezena,centena,milhar
num = int(input("Digite um numero de 0 a 9999: "))
#n = str(num).strip()
#space = " ".join(n)
#lista = space.split()

#print (len(lista[0]))

#print("Unidade: {}".format(lista[3]))
#print("Dezena: {}".format(lista[2]))
#print("centana:{}".format(lista[1]))
#print("Milhar: {}".format(lista[0]))

#Uma 2 forma de se fazer sem da erro colcando abaixo de um numero que tenha 4 unidades 
u = num // 1 % 10 
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10 

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("centana:{}".format(c))
print("Milhar: {}".format(m))