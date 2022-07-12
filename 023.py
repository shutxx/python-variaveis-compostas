pessoas = {'Nome': 'Allan', 'Sexo': 'M', 'Idade': 27}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print('--' * 20)
# printa as chaves do dicionario antes do ':'
print(pessoas.keys())
print('--' * 20)
# printa todos os itens do dicionario
print(pessoas.items())
print('--' * 20)
# o k imprime as chaves do dicionario o v imprime o itens dele
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['Sexo']
print('--' * 20)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('--' * 20)
pessoas['Nome'] = 'leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
