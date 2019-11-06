"""
    solitar a idade do carro do usuário e , em seguida, escrevermmos novo se o carro tiver menos de três anos.
    caso contrário velho
"""

idade = int(input('Digite a idade do seu carro: '))

if idade <= 3:
    print('seu carro é novo')
if idade > 3:
    print('Seu carro é velho')
