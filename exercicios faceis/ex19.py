# 19. Solicite nomes at´e que o usu´ ario digite ”sair”. Armazene em uma lista e imprima.
nomes = []

while True:
    nome = input('Digite um nome (ou "sair" para encerrar): ').strip().lower()
    if nome == 'sair':
        break
    nomes.append(nome)

print("Nomes digitados:")
for nome in nomes:
    print(nome)


