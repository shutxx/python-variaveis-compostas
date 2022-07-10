valores = list()
pares = list()
ímpares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'A lista completa é {valores}')
if len(pares) == 0:
    print('a lista de pares esta vazia...')
else:
    print(f'A lista de pares é {pares}')
if len(ímpares) == 0:
    print('A lista de ímpares esta vazia...')
else:
    print(f'A lista de ímpares é {ímpares}')