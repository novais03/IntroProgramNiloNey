"""
For

- Um estrutura de repetição especialmente para listas
- A cada repetição utiliza um elemento diferente

# Listagem 6.24 - Impressão de todos so elementos de um lista
l = [8, 9, 15]
for i in l:
    print(i)

# resultado
8
9
15


# Listagem 6.25 - Impressão de todos os elementos da lista com while

l = [8, 9, 15]
x = 0
while x < len(l):
    e = l[x]
    print(e)
    x += 1
# Resultado
8
9
15

OBS:
- utililzamos "for" quando quisermos processar elementos de uma lista, um a um.
- "while" é indicado para repetições nas quais não sabemos quantas vezes vamos repetir
  ou onde manipulamos o indice de forma não sequêncial
- A instrução "break" também interrompe o "for".
"""

# listagem 6.26 - Pesquisa usando for
L = [7, 9, 10, 12]
p = int(input("Digíte um número a pesquisar: "))
achou = False
for e in L:
    if e == p:
        print("Elemento encontrado!")
        achou = True
        break # interrompe a busca depois do elemento ser encontrado
if achou == False:
    print("Elemento não encontrado!")
