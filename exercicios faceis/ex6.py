''' 
6. Solicite 5 numeros ao usuario e armazene em uma lista. Em seguida, imprima o
maior e o menor numero.
'''
numeros = []

for i in range(5):
    numero = input(f'Digite o {i + 1}º número: ')
    numeros.append(numero)

print(f'Lista: {numeros}')
print(f'Maior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')