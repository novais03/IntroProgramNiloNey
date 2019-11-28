"""
Filas
- Podemos usar listas como filas.
- Em uma fila, a incluão sempre acontece no fim da lista, e a remoção acontece no inicío;
- Dizemos o primeiro a chegar e último as sair. (FIFO - First In First Out).
"""

ultimo = 10
fila = list(range(1,ultimo+1))

while True:
    print(f'\nExsitem {len(fila)} clientes na fila: ')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao Fim da fila,')
    print('Digite A para Atendimento. S para Sair.')

    operacao = input("Operação (F, A ou S):")

    indice = 0
    sair = False

    while indice < len(operacao):
        if operacao[indice] == "A" or operacao == "a":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print('Cliente %d atendido.' % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[indice] == "F" or operacao == "f":
            ultimo += 1 # Incrementa o ticket para atender.
            fila.append(ultimo)
        elif operacao[indice] == "S" or operacao == "s":
            sair = True
        else:
            print("Operação inválida! Digite apenas f, A ou S")
        indice += 1
    if (sair):
        break