def leiaDinheiro(preco):
    validade = False
    while not validade:
        valor = str(input(preco)).strip().replace(",",".")
        if valor.isalpha() or valor == '':#se valor for letras ou tiver espaço vai retornar erro
            print(f"\33[0;31mERRO: '{preco}' e um preço invalido! \33[m")
        else:
            validade = True
            return float(valor)
