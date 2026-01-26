#refazer o desafio 35 dos triangulos acrescentado o recurso de mostra que tipo de triangulo sera formado
#equilatero: todos os lados iguais
#isosceles: dois lados iguais
#escalenos: todos os lados diferentes
print("-=-"*28)
print("|Aplicativo de consulta de retas a favor da formaçao de triangulos e classificaçao |")
print("-=-"*28)
r1 = float(input(("Comprimento da 1 reta: ")))
r2 = float(input("Comprimento da 1 reta: "))
r3 = float(input("Comprimento da 1 reta: "))
if (r1 + r2 > r3) and (r1+r3 > r2 ) and (r2 + r3 > r1):
    print("com os comprimetos {:.0f}, {:.0f}, {:.0f}, e possivel forma um triangulo".format(r1,r2,r3))
    if r1 == r2 == r3:
        print("Esse triangulo ele e classificado como EQUILATERO ")
        print("Todos os lados sao iguais")
#possivel tambem usar no escaleno r1 != r2 != r3 != r1  
    elif (r1 == r2 ) or (r2 == r3) or (r3 == r1):
        print("Esse triangulo ele e classificado como ISOSCELES ")
        print("Apenas dois lados iguais")

    else:
        print("Esse triangulo ele e classificado como ESCALENO")
        print("todos os lados diferentes")
else:
    print("Com os comprimentos {:.0f},{:.0f},{:.0f}, nao e possivel forma um triangulo :( .".format(r1,r2,r3))