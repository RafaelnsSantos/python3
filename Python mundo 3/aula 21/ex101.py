#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
#de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
# e possivel importar biblioteca dentro da funçao economizando memoria
def voto(nascimento):
    from datetime import date
    ano_atual= date.today().year
    idade = ano_atual - nascimento
    if 18 <= idade < 70:
        return f"com {idade} Voto e OBRIGATORIO. "
    elif idade < 16:
        return f'com {idade} voce NAO PODE VOTAR AINDA'
    else:
        return f"Com {idade} voto e OPCIONAL."
    
#programa principal
nasc = int(input("Ano de nascimento: "))
print(voto(nasc))

