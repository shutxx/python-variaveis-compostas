pessoas = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda S ou N.')
    if resp == 'N':
        break  # leitura dos dados
print('-=' * 20)
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('lista de pessoas que estão a cima da média: ')
for p in pessoas:
    if p['Idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<<<FIM>>>')  # analisando e informando resultados 
