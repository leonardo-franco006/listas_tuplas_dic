''' 
2. Solicite ao usuário 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha.
'''
nome1 = input('Escreva um nome: ')
nome2 = input('Escreva um nome: ')
nome3 = input('Escreva um nome: ')
nome4 = input('Escreva um nome: ')
nome5 = input('Escreva um nome: ')

lista = [nome1, nome2, nome3, nome4, nome5]

print('--> Os nomes selecionados foram:')

for i in range(len(lista)):
    print(lista[i])