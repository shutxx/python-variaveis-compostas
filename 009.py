num = [2, 9, 7, 8]
print(num)
# adicionar valor a lista
num.append(7)
print(num)
# ordena do menor para maior
num.sort()
print(num)
# ordena do maior para o menor
num.sort(reverse=True)
print(num)
# adiciona o 0 na segunda posição
num.insert(2, 0)
print(num)
# remove na segunda posição
num.pop(2)
print(num)
# remore o primeiro iten informado
num.remove(7)
num.insert(4, 4)
print(num)
if 4 in num:
    num.remove(4)
    print('numero 4 removido')
    print(num)
else:
    print('Não achei o número 4.')
