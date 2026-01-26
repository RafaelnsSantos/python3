#crie um programa que tenha uma funçao chamada fatorial()
#que receba dois parametros: o primeiro que indique o numero a calcular o fatorial
#o segundo chamado show que sera um valor logico(opcional) 
# indicando se sera mostrado ou nao na tela o processo de calculo do fatorial

def fatorial(n,show=False):
    """
    Docstring for fatorial
    calcula o fatorial de um numero.
    :param n: o numero a ser calculado
    :param show: o show se estiver false ele retorna o resultado de n diretamente se estiver true retrona adjunto do calculo
    :return: o valor do fatorial de um numero n
    """
#se n for igual a 0 ou n igual a 1 retorne para quem pediu 1 
    if n == 0 or n == 1:
        return 1 
    #se nao resultado = 1 e se show = verdadeiro c vai percorer inicio = n ate 0 indo de  1 em 1 
    #depois vai printar c x e dando resultado *= c que ta variando depois retornando resultado
    else:
        resultado = 1
        if show == True:
            print(f"{n}! =",end= '')
            for c in range (n,0,-1):
                if c > 1:
                    print(f"{c} ", end = "x ")
                else:
                    print(f"{c}",end= " = ")
                resultado *=c
            return resultado
        #se for falso retorne apenas resultado
        if show == False:
            for c in range (n,0,-1):
                resultado *= c
            print(f"{n}! = ", end = ' ')
            return resultado


numero = int(input("digite um numero para ver o fatorial: "))
print(fatorial( numero,show=False))
help(fatorial)
