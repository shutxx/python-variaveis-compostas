time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    partidas.clear()
    for cont in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {cont + 1}?: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break  # informações dos jogadores
print('-=' * 20)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 20)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 20)
while True:
    busca = int(input('Mostrar dados de qual jogador: [999] para parar.'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código de {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca] ["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-=' * 20)
print('FIM...')
