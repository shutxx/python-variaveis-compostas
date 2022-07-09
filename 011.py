valores = list()
maior= menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na {cont}º: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Você digitou os valores {valores}')
# print(f'O maior valor digitado foi {max(valores)}')
# print(f'O menor valor digitado foi {min(valores)}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}º...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}º...', end='')
