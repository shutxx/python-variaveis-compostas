valores = list()
valores.append(5)
valores.append(9)
valores.append(3)
for v in valores:
    print(f'{v}...', end='')
print(' ')
for c, v in enumerate(valores):
    print(f'{c}º {v}')

valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input('Digite um número: ')))
print(valores2)
# cria uma copia de a dentro de b
a = [0, 5, 8, 9]
b = a[:]
print(b)
