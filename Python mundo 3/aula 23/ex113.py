#reescreva a funçao leiaint() que fizemos no desafio 104, incluindo agora a 
#possibilidade da digitaçao de um número de tipo inválido. aproveite e crie também uma
#funçao leiafloat() com a mesma funcionalidade.
def leiaint(n=''):
    while True:
        try:
            valor = int(input(n))
            return valor
        except (ValueError, TypeError):
            print("\033[0;31mtivemos um poblema com os tipos de dados que voce digitou. \033[m")
        except (KeyboardInterrupt):
            print("\n\033[0;31mO usuario preferiu nao informa os dados! \033[m ")
            return 0


def leiafloat(n=''):
    while True:
        try:
            valor = float(input(n))
            return valor
        except (ValueError, TypeError):
            print("\033[0;31mtivemos um poblema com os tipos de dados que voce digitou. \033[m")
        except (KeyboardInterrupt):
             print("\n\033[0;31mO usuario preferiu nao informa os dados! \033[m")
             return 0.0

numero = leiaint("Digite um numero inteiro: ")
real = leiafloat("Digite um valor real: ")
print(f"O valor inteiro digitado: {numero} e o real foi: {real}")