# 23. Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a ordem.

nomes_rep = ['leo', 'luisa', 'marcelo', 'emily', 'leo', 'vini', 'emily', 'beto']
nomes_unicos = []
vistos = set()

for nome in nomes_rep:
    if nome not in vistos:
        nomes_unicos.append(nome)
        vistos.add(nome)

print(nomes_unicos)