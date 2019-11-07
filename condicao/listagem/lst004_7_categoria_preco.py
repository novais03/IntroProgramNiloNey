# coding=utf-8
"""
    Exemplo de estruturas aninhadas
    faça um programa que leia a categoria de um produto e determine o preço pela tabela.
    Categoria   preço
        1       10.00
        2       18.00
        3       23.00
        4       26.00
        5       31.00
"""
categoria = int(input('Digite a categoria do produto: '))
if categoria == 1:
    preco = 10.00
else:
    if categoria == 2:
        preco = 18.00
    else:
        if categoria == 3:
            preco = 23.00
        else:
            if categoria == 4:
                preco = 26.00
            else:
                if categoria == 5:
                    preco = 31.00
                else:
                    print('Categoria inválida, digite um valor entre 1 e 5!')
                    preco = 0

print('O preço do produto é: R$ %6.2f' % preco)
