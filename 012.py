listanum = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Número adicionado com sucesso')
    else:
        print('Número duplicado! não pode ser adicionado')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
listanum.sort()
print(f'Você adicionou os valores {listanum}')