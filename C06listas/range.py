"""
range()

    utilizado para gerar listas;

# Listagem 6.29 - Uso da função range

for v in range(10):
    print(v)

# Resultado

0
1
2
3
4
5
6
7
8
9

# Listagem 6.28 - Usando função range com intervalos

# podemo incluir qual é o primeiro a gerar range(primeiro_valor, ultimo_valor)
for x in range(5, 8):
    print(x)
# Resultado
5
6
7

# Exemplo 3 - usando saltos na lista

# listagem 6.29 - Uso da finção range com saltos
for t in range(3,33, 3):
    print(t, end=" ") # end= - imprime um número ao lado do outro, e imprime um valor entre eles, no caso aqui espaço
print()
"""

# lsitagem 6.30 - transformação de resultado de range em uma lista

L = list(range(100, 1100, 50))
print(L)