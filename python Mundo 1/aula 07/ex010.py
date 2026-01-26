#crie um programa que leia quanto de dinheiro uma pessoa tenha na carteira e mostre
#quantos dolares ela pode compra , considerar us$1,00 = R$3,27
print("="*30)
print("|             conversor      |")
print("="*30)

n = float(input("quantos reais voce quer converter?:R$"))
dolar = n /5,37

print("Voce pediu para converter R${:.2f} que da cerca de usd${:.2f} ".format(n,dolar))
print("cotaçao atual do dia 10/01/2026 cerca de 1 dolar = R$5,37")