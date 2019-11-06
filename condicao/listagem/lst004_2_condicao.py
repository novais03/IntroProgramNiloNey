def maior_de_dois_numeros(a,b):
    """
    ler dois valores e imprimir o maio deles, apresentado
    :return: maior
    """
    if a > b:
        return a
    if b > a:
        return b

if __name__ == '__main__':
    print(maior_de_dois_numeros(9,9))