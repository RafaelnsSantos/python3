#crie um programa que tenha uma tupla com varias palavras (nao usa acentos) depois disso voce deve mostra para cada palavra
#quais sao suas vogais.
tupla = ('Sol','Lua','Computador','Pizza','Carro','Escola','Chave','Montanha','Livro','Janela','Relogio','Cachorro')

#vogais = ("A, E I O U")
#c ele vai anda pelas palavras no caso sol lua etc etc
for c in tupla:
    print(f'na palavra {c.upper()} temos:',end = ' ')
    #letras vai anda pelas letras literalmente
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f"{letra.lower()}",end = ' ')
    print()