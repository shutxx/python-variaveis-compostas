times = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional',
         'Fluminense', 'São Paulo', 'Flamengo', 'Bota Fogo', 'Santos', 'Avaí',
         'Coritiba', 'América-MG', 'Bragantino', 'Ceará-SC', 'Atlético-GO', 'Goiás',
         'Cuiaba', 'Juventude', 'Fortaleza')
print('-=' * 20)
print(f'Lista de times: {times}')
print('-=' * 20)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Corinthians está na {times.index("Corinthians")+1}º posição')
