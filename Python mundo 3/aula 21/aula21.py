#help(print)

'''def contador (i,f,p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i 
    while c <= f:
        print(f'{c}',end= ' ')
        c += p 
help(contador)'''

#paramentros opcionais
'''def somar(a=0,b=0,c=0):
    """
    Faz a soma de tres valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

#somar(3,2,5)
#somar(8,4)
#somar()'''

#escopo de variaveis
#escopo local ele so funciona dentro da funcao
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# e escopo global ela funciona em todo o programa
#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()'''


"""#variaveis globais e locais 
def teste(b):
    global a # o global faz com que a variavel a seja global e nao local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
#Programa principal
a = 5
teste(a)
print(f'A fora vale {a}')"""
'''def soma (a=0,b=0,c=0):
    s = a + b + c
    return s
r1 = soma(3,2,5)
r2 = soma(2,2)
r3 = soma(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')'''

'''def fatorial (num = 1):
    f = 1
    for c in range(num,0,-1):
        f *=c 
    return f #return pode retorna verdadeiro ou falso
n = int(input("digite um numero: "))
print(f"O fatorial do numero {n} e igual a {fatorial(n)}")'''

def parouimpar (n=0):
    if n%2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um numero: "))
if parouimpar(numero):
    print("par")
else:
    print("Impar")  