"""
Pilha

- Podemos usar listas como pilha.
- Em uma pilha, a incluão sempre acontece no fim da lista, e a remoção acontece no fim;
- Dizemos o Último a chegar e primeiro as sair. (Lifo - Last In First Out).
"""
# Listagem 6.22 - Pilha se Pratos
prato = 5
pilha = list(range(1,prato+1))

while True:
    print(f'\nExsitem {len(pilha)} pratos na pilha: ')
    print(f'pilha atual: {pilha}')
    print('Digite E para empilhar um novo prato na pilha,')
    print('Digite D para Desempilhar. S para Sair.')

    operacao = input("Operação (E, D ou S):")

    if operacao == "D" or operacao == "d":
        if len(pilha) > 0:
            lavado = pilha.pop(0)
            print('Prato %d lavado.' % lavado)
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operacao == "E" or operacao == "e":
        prato += 1 # novo prato.
        pilha.append(prato)
    elif operacao == "S" or operacao == "s":
        break
    else:
        print("Operação inválida! Digite apenas f, A ou S")
