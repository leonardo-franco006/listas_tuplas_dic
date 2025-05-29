# 21. Solicite ao usuario 10 numeros, 
# armazene em uma lista e remova todos os numeros pares usando remove.

numeros = []

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    numeros.append(num)
    if num % 2 == 0:
        numeros.remove(num)

print('Números ímpares: ')
for num in numeros:
    print(num)