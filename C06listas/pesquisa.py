"""
Pesquisa

- Podemos pesquisar se um elemento está ou não está em uma lista
"""

# Listagem 6.23 - Pesquisa sequencial
l = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0
achou = False
while x < len(l):
    if l[x] == p:
        achou = True
    x += 1
if achou:
    print("%d achado na posição %d" % (p,x))
else:
    print(" %d não encontrado" % p)
