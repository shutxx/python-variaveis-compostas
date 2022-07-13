# jogador = [[nome: ],[gols [0, 1, 2, 3, 4,]]
jogos = dict()
jogos['Nome'] = str(input('Nome do jogador: '))
jogos['Partidas'] = int(input(f'Quantas partidas {jogos["Nome"]} jogou?: '))
if jogos['Partidas'] != 0:
    totgol = 0
    for part in range(0, jogos['Partidas']):
        jogos['Gols'] = int(input(f'Quantos gols na partida {part + 1}º?: '))
        totgol += jogos['Gols']
        jogos['Gols'] = totgol
print(jogos)


