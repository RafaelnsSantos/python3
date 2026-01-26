#Cria uma tupla preenchida com os 20 primeiros colocados da Tabala do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
# D) em que posição na tabela está o time da Chapecoense

brasileirao = 'Athletico-PR','Atlético-MG','Bahia','Botafogo','Bragantino','Chapecoense','Corinthians','Coritiba','Cruzeiro','Flamengo','Fluminense','Grêmio','Internacional','Mirassol','Palmeiras','Remo','Santos','São Paulo','Vasco','Vitória'

print("-=-"*40)
print(f"Os 5 primeiros colocados do brasileirao de 2026: {brasileirao[0:5]}")
print("-=-"*40)

#poderia ser tambem -4: 
print("-=-"*40)
print(f'Os 4 ultimos colocados do brasileirao de 2026 : {brasileirao[16:]}')
print("-=-"*40)

print("-=-"*48)
print(f'Os times em ordem alfabetica: {sorted(brasileirao)}')
print("-=-"*48)

print("-=-"*11)
print(f'O Chapecoense esta na posiçao {brasileirao.index('Chapecoense')+1}')
print("-=-"*11)
