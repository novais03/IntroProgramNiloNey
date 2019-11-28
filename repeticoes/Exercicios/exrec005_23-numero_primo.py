"""
    Escreva um programa que leia um número e verifique se ele é o unão um númeor primo.

    Para fazer a verificação  clacule o resto da divisão do número por 2 e depois por todos os números impares até o
    número lido.

    premissa:
    1) 0 e 1 --> não são primos
    2) 2 é o único número par que é primo

      Exemplos:

    1) O número 161:
    não é par, portanto não é divisível por 2;
    1+6+1 = 8, portanto não é divisível por 3;
    não termina em 0 nem em 5, portanto não é divisível por 5;
    por 7:  161 / 7 = 23, com resto zero, logo 161 é divisível por 7,
    >>>e portanto não é um número primo.

    2) O número 113:
    não é par, portanto não é divisível por 2;
    1+1+3 = 5, portanto não é divisível por 3;
    não termina em 0 nem em 5, portanto não é divisível por 5;
    por 7:  113 / 7 = 16, com resto 1. O quociente (16) ainda é maior que o divisor (7).
    por 11:  113 / 11 = 10, com resto 3. O quociente (10) é menor que o divisor (11),
    e além disso o resto é diferente de zero (o resto vale 3),
    >>> portanto 113 é um número primo.
"""
numero = int(input('digite um núemro maior interio..:'))

if numero < 0:
    print('Número inválidp! Digite apenas valores positivos.')
elif numero == 0 or numero == 1:
    print('O %d é um caso especial' % numero)
else:
    if numero == 2:
        print('2 é primo"')
    elif numero % 2 == 0:
        print('Não é primo. 2 é o único número para que é primo.')
    else:
        x = 3
        while x < numero:
            if numero % x == 0:
                break
            x = x+1
        if numero == x:
            print('%d é primo' % numero)
        else:
            print('%d não é primo' % numero)



