#aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
while True:
    campeonato = {}
    jogador = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas o {jogador} jogou? "))

    gols = []
    for c in range (partidas):
        gol = int(input(f"Quantos gol ele fez na {c + 1} partida: "))
        gols.append(gol)

    campeonato['gols'] = gols
    campeonato['jogador'] = jogador
    campeonato['partidas'] = partidas
    campeonato['total'] = sum(gols)

    jogadores.append(campeonato.copy())

    escolha_user = ' '
    while escolha_user not in 'SN':
        escolha_user = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if escolha_user in 'SN':
            break

    if escolha_user == 'N':
        break

print('-=-'*15)
print("NO NOME         GOLS       TOTAL")
print("---"*15)
#print(f"{'Nº':<4}{'nome':<15}{'gols':<20}{'Total:<6'}")
for i, c in enumerate(jogadores):#c vai ta percorrendo jogadores e vai ta pritando oque foi pedido i percorre o enumerante
        print(f" {i} {c['jogador']} {c['gols']} {c['total']}")
while True:
    opçao = int(input("Mostra dados de qual jogador?(999 para parar(STOP)): "))
    if opçao == 999:
         break
    if opçao >= len(jogadores):
         print(f"Erro nao existe jogador com codigo: {opçao}")
    else:
        print(f"levatamento do jogador {jogadores[opçao]['jogador']}")
        #P percorre enumerante e g percorre jogadores gols
        for p , g in enumerate(jogadores[opçao]['gols']):
            print(f'no jogo {p+1} fez {g} gols')
