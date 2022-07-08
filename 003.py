cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[n]}')
