lista = list()
cont = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    lista.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        cont += 1
    if resp == 'N':
        break
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não foi encontrado na lista')