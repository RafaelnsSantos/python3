#faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio
#Indo de 10 ate 0 , com uma pauas de 1 segundo entre eles
import time
print("A queima de fogos vai começa em:")
for c in range (10,0,-1):
    print(c)
    time.sleep(1)
print("FELIZ ANO NOVO!!!")
