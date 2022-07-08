# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
lanche1 = ('Sorvete', 'Refrigerante', 'Batata Frita')
n = int(input('Qual lancher vce quer: [0, 3] '))
print(lanche[n])
print(sorted(lanche[0:2]))
print('-=' * 20)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-=' * 20)
for cont in range(0, len(lanche1)):
    print(f'Eu vou comer {lanche1[cont]}')
print('-=' * 20)
for pos, comi in enumerate(lanche1):
    print(f'Eu vou comer {pos}º {comi}')
