#adapte o codigo do desafio 107, criando uma função adicional 
# chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.aumentar(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos R${moeda.moeda(moeda.diminuir(p, 13))}')
