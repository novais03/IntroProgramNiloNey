
"""
Escreva um programa que leia dois números e que pergunte qual operação deseja realizar.
    (+) Soma
    (-) Subtração
    (*) multiplicação
    (/) divisão
Exiba o resultado da operação solicitada

a = int(input('digite o primeiro número..: '))
b = int(input('digite o segundo número...: '))
operacao = input('Digite a operação a realizar (+,-,* ou /): ')


if operacao == ""+"":
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

print('O resultado do é..: %f' % resultado)

print('Esolha uma opção...: %d' % (a + b))
"""

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operacao = input("Digite a operação a realizar (+,-,* ou /):")

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)
