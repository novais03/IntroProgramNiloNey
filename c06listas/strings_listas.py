"""
Strings - Usadas em listas
# Exemplo

S = ['maçãs', 'peras', 'kiwis']
print(len(S))

print(S[0])
print(S[1])
print(S[2])

# Lista com strings acessando letras
print(S[0][0])
print(S[1][1])
print(S[2][2])

# impressão letra a letra

for i in S:
    for letra in i:
        print(letra)
# lista dentro de listas (Lista de compra)

# Exemplo 1
produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
print(compras) # temos a lista compra com 03 elementos, ,mas casa elemento é um lista à parte

for i in compras:
    print("Produto....: %s:" % i[0])
    print("Quantidade.: %d:" % i[1])
    print("Preço......: %f:" % i[2])
    print()

"""
# Exemplo 2
compras = []
while True:
    produto = input("Produto: ")
    produto = produto.upper()
    if produto == "FIM":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for i in compras:
    print(f'{i[0]:20s} x {i[1]:5d} {i[2]:5.2f} {i[1]*i[2]:6.2f}')
    soma += i[1] * i[2]
print("Total: %7.2f" % soma)
