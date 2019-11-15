"""
Imprimir as tabuadas de multiplicação de 1 a 10.


Print the multiplication tables from 1 to 10.

"""
tabuada = 1
while tabuada <= 10:
    numero =1
    print("")
    while numero <=10:
        print('%d x %d = %d' %(numero, tabuada, numero * tabuada))
        numero +=1
    tabuada +=1
