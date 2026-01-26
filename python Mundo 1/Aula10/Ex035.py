#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se eles podem
#Ou nao formar um triangulo
print("="*67)
print("|Aplicativo de consulta de retas a favor da formaçao de triangulos|")
print("="*67)
r1 = float(input("Comprimento da 1 reta: "))
r2 = float(input("Comprimento da 2 reta: "))
r3 = float(input("Comprimento da 3 reta: "))

if (r1 + r2 > r3) and (r1+r3 > r2 ) and (r2 + r3 > r1):
    print("com os comprimetos {:.0f}, {:.0f}, {:.0f}, e possivel forma um triangulo".format(r1,r2,r3))
else:
    print("Com os comprimentos {:.0f},{:.0f},{:.0f}, nao e possivel forma um triangulo :( .".format(r1,r2,r3))