lista = ('Lápis', 1.75,
         'Caderno', 15.50,
         'Estojo', 5.50,
         'Mochila', 150.75,
         'Livro', 34.90,
         'Borracha', 0.90,
         'Compasso', 9.99)
print(f'{"LISTAGEM DE PREÇO":^40}')
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R$:{lista[item]:>7.2f}')
