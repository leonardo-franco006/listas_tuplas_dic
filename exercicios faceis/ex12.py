# 12. Leia 5 numeros do usuario e verifique se cada um deles é maior que 10.

numeros = []

for i in range(5):
    num = float(input(f'Digite o {i+1}º número: '))
    numeros.append(num)

for i, num in enumerate(numeros): 
    if num > 10:
        print(f'O {i+1}º número é maior que 10')
    else:
        print(f'O {i+1}º número é menor que 10')
print(numeros)