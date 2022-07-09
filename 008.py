palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for cont in palavras:
    print(f'\nNa palavra {cont.upper()} temos: ', end='')
    for letra in cont:
       if letra.lower() in 'aeiou':
            print(letra, end=' ')
