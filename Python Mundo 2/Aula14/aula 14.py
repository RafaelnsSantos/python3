#replicando o for no while tendo limite:
#c = de contar coloquei ele começando por 1 
#c = 1 
#        fim
#while c < 10:
    #print(c)
# e preciso fazer ele somar +1 ate que seja o fim que no caso e 10
    #c += 1

#Utilizando o while como uma forma de continua ate quando o usuario quiser
#utilziar o while ou for dependendo da necessidade for = se tiver um limite , 
# while sem nao tiver limite.
n1 = 0
soma = 0
r = 'S'
while r == 'S':
    n = int(input(("digite um valor: ")))
    soma += n 
    r = str(input("quer continuar?[S/N]")).strip().upper()
print("A soma dos numeros foi: {}".format(n))


