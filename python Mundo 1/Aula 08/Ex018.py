#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input("digite um angulo que deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("Angulo {:.2f} tem o seno: {:.2f} \n cosseno: {:.2f} \n tangente: {:.2f}".format(angulo,seno,cosseno,tan))
