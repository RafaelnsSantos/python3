#Escreva um program que leia um numero inteiro qualquer e peça para o usuario escolher
#qual sera a base de conversao: - 1 binario , 2 octal , 3 hexadecimal
print("-=-"*7)
print("|Conversor de numeros|")
print("-=-"*7)
n = int(input("Escolha um numero inteiro: "))
print("-=-"*10)
print("Escolha uma das bases para a conversao do numero {}".format(n))
print("[1] Conversao para BINARIO \n[2] Conversao para OCTAL \n[3] Conversao para HEXADECIMAL")
print("-=-"*10)
escolha_user = int(input("sua escolha: "))
binario = bin(n).replace("0b","")
octal = oct(n).replace("0o","")
hexadecimal = hex(n).replace("0x","")
if escolha_user == 1:
    print("{} convertido para BINARIO e igual a {}".format(n,binario))
elif escolha_user == 2:
    print("{} convertido para OCTAL e igual a {}".format(n,octal))
elif escolha_user == 3:
    print("{} Convertido para HEXADECIMAL e igual a {} ".format(n,hexadecimal))
elif escolha_user > 3 or escolha_user < 0:
    print("Opçao invalida!")
