n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite último número: '))
num = (n1, n2, n3, n4)
if 9 in num:
    print(f'O valor 9 aparece {num.count(9)} vezes')
else:
    print('O valor 9 não foi digitado em nem uma posição')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º')
else:
    print('O valor 3  não foi digitado em nem uma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
