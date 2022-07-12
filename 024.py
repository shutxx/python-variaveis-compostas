brasil = []
estado1 = {'Uf': 'Parana', 'Sigla': 'PR'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['Uf'])
print(brasil[1]['Sigla'])
print('-=' * 20)
estado = dict()
braz = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    braz.append(estado.copy())
print(braz)
print('-=' * 20)
for e in braz:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print('-=' * 20)
for e in braz:
    for v in e.values():
        print(v, end=' ')
    print()