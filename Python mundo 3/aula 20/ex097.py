#faça um programa que tenha uma funçao chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
#ex: escreva('Olá, Mundo!')# Saída:
# ~~~~~~~~~~~~~
#   Olá, Mundo!
# ~~~~~~~~~~~~~
#adatpataçao vai receber o tamando de len(txt) assim se adaptando a o tamanho
def escreva (txt):
    adaptaçao = len(txt)
    print('~'*adaptaçao)
    print(txt)
    print('~'*adaptaçao)


#programa principal
txt = str(input("Digite algo: ")).strip()
escreva(txt)