# 13. Crie uma lista com os numeros de 1 a 10 usando range() e imprima somente os pares.

numeros = list(range(1, 11))

for i, num in enumerate(numeros):
    if num % 2 == 0:
        print(num)
