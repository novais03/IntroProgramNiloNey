"""
Exemplo de uso de Estutururas aninhdas - ou seja, um IF dentro de outro If.
    Calcular conta de telefone da empresa Tchau. Os planos da empresa Tchau são bem interessantes
    e oferecem preços diferentes de acordo com a quantidade de minutos usados por mês.

        Abaixo de 200 minutos é de R$ 0,20 por minuto
        Entre 200 e 400 minutos é de R$ 0,18 pro minuto
        Acima de 400 minutos é de R$ 0,15 por minuto
    O programa deve resolver este problema:
"""
minutos = int(input('Digite a quantidade de minutos..: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15

print('Você vai pagar este mês: R$ %6.2f' % (minutos * preco))
