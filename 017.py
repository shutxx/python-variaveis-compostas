teste = list()
teste.append('Allan')
teste.append(27)
galera = list()
galera.append(teste[:])
teste[0] = 'Eduarda'
teste[1] = 22
galera.append(teste[:])
print(galera)
amigos = [['Ana', 22], ['Marcio', 15], ['Joaquin', 15], ['Mateus', 25]]
print(amigos)
for p in amigos:
    print(f'{p[0]} tem {p[1]} anos de idade.')
facul = list()
dados = list()
for cont in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    # [:] faz copias de dado
    facul.append(dados[:])
    dados.clear()
print(facul)
totmai = totmen = 0
for pess in facul:
    if pess[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{pess[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')