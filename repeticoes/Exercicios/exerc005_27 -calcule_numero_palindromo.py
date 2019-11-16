# Para resolver este problema, podemos usar strings, apresentadas na seção 3.4 do livro
# Veja que estamos lendo o número sem convertê-lo para int ou float,
# desta forma o valor de s será uma string
s = input ("Digite o número a verificar, sem espaços:")
i = 0
f = len(s)-1 # posição do último caracter da string
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print("%s é palíndromo" % s)
else:
    print("%s não é palíndromo" % s)