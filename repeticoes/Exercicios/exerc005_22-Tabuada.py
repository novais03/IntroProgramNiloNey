"""
Escreva um programa que exiba um lista de opçoes menu:
Adição, Subtração, Multiplicação, divisão e sair.

Imprima a tabuada da operação escolhida.

repita até que a opção saída seja escolhida

"""
# menu

while True:
    print("(+) Adição")
    print("(-) Subtração")
    print("(*) Multiplcação")
    print("(/) Divisão")
    print("(0) Sair")
    opcao = input("Digite uma das opçãos..: ")
    if opcao == "0":
        break
    elif opcao == "+" or opcao == "-" or opcao == "/" or opcao =="*":
        tabuada = int(input('tabuada de.: '))
        nunero = 1
        while nunero <=10:
            if opcao == "+":
                print('%d + %d = %d' %(nunero, tabuada, nunero + tabuada))
            elif opcao == "-":
                print('%d - %d = %d' % (nunero, tabuada, nunero - tabuada))
            elif opcao == "*":
                print('%d * %d = %d' % (nunero, tabuada, nunero * tabuada))
            elif opcao == "/":
                print('%d / %d = %d' % (nunero, tabuada, nunero / tabuada))
            nunero += 1
    else:
        prin("Opção inválida!")
    print()






