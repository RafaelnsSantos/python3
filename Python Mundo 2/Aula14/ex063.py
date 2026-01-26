#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequencia fibonacci ex 0 1 1 2 3 5 8
#c vai soma a , b depois a vai vira b e b vai vira c 
print("Sequencia de fibonacci")
a = 0
b = 1
co = 3
fim = int(input("quantos voce quer mostra? "))
print("{} {}".format(a,b),end = ' ')
while co <= fim:
   co += 1
   c = a + b
   a = b
   b = c
   print("{}".format(c),end = ' ')
