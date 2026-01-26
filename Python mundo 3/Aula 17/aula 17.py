#num = []
#num.append(2)
#num.sort()
#num.remove(2)
#print(f"{len(num)}")
#print(num)
#forma simples de por valores na lista:
#for cont in range (0,5):
    #num.append(int(input("Digite um valor: ")))
#
#num.append(3)
#num.append(2)
#num.append(10)
#
#for v, c in enumerate(num):
    #print(f"na posiçao {v} encontrei {c}!")
#print("Cheguei ao final da lista!!")


#se voce atribuir uma lista a uma variavel e depois muda uma coisa de uma lista vai mudar tambem a lista atribuida
#o python tem ligaçao
#para criar uma copia usa-se b = a [:]
a = [2,3,4,7]
b = a
b[2] = 8
print(f"lista A: {a}")
print(f"Lista B: {b}")


