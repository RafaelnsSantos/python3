#faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o 
# manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores.
import time
def escreva (txt):
    adaptaçao = len(txt)
    print('\033[0;32;42m~\033[m'*adaptaçao)
    print(f"\033[0;32;42m{txt}\033[m")
    print('\033[0;32;42m~\033[m'*adaptaçao)

def ajuda (a):
    while True:
        #print("\033[34m")
        escreva("SISTEMA DE AJUDA PyHELP")
        a = input("Funçao ou biblioteca > ").lower().strip()
        if a == 'fim':
            escreva("ATE LOGO!")
            break
        escreva(f"Acessando o manual do comando '{a}' ")
        time.sleep(1)
        help(f"{a}")
        time.sleep(1.5)

ajuda("")

#soluçao do guanabara
'''def ajuda(com):
    help(com)
def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!')
        break
    else:
        ajuda(comando)'''
#fim do guanabara