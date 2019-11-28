
# escreva um programa que calcule a raiz quadrada de um número.
# utilize o método de newton para opter a raiz.

# A fórmula correta é p = ( b + ( n / b ) ) / 2  (b=2)
# A função abs foi utilizada para calcular o valor absoluto de um número,
# ou seja, seu valor sem sinal.
# Exemplos: abs(1) retorna 1 e abs(-1) retorna 1
# para quando a diferença absoluta ente n e o quadrado de p for menor que 0.0001
# formula abs(n - (p * P) < 0.0001

n = float(input('Digite um numero: '))
b = 2
while abs(n - (b * b)) > 0.0001:
    p = (b +(n / b))/2
    b = p

print("a raiz quadrada de %4.2f aprximadamente % 8.4f" % (n, p) )