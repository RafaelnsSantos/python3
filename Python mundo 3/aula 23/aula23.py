#tratamento de erro
try:
    a = int(input("Numerador: "))
    b = int(input("Denomiador: "))
    r = a/b
except (ValueError, TypeError):
    print(f"tivemos um poblema com os tipos de dados que voce digitou. ")
except ZeroDivisionError:
    print("Nao e possivel dividir um numero por zero")
except KeyboardInterrupt:
    print("O usuario preferiu nao informa os dados!")
else:
    print(f'o resultado e {r}') 
finally:
    print("volte sempre muito obrigado")