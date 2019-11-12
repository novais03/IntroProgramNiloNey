
"""
Escreva um programa que leia dois números e que pergunte qual operação deseja realizar.
    (+) Soma
    (-) Subtração
    (*) multiplicação
    (/) divisão
Exiba o resultado da operação solicitada
"""
a = float(input('digite o primeiro número..: '))
b = float(input('digite o segundo número...: '))
operacao = input('Digite a operação a realizar (+,-,* ou /): ')

if operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b
elif operacao == '/':
    resultado = a / b
else:
    print('Opção invalida!')
    resutlado = 0

print("O resultado do é..: %6.2f" % resultado)

