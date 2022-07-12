from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('-=' * 20)
print('Valores sorteados:')
print('-=' * 20)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    if v[1] >= 6:
        print('CRITICO')
    elif v[1] <= 2:
        print('MISS')
    sleep(1)