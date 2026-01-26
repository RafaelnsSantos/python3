#faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

#aqui eu vou criar a função area que vai receber dois parametros largura e comprimento e depois vou calcular 
# a area do terreno tendo como formula largura x comprimento e depois mostrar o resultado na tela.
def area (largura,comprimento):
    a = largura * comprimento
    print(f'area do terreno {largura} x {comprimento} = {a} m2')


#programa principal
largura = float(input("Largura: ")) 
comprimento = float(input("comprimento:"))
area(largura,comprimento) # aqui estou chamando a função  area e passando os parametros largura e comprimento.
