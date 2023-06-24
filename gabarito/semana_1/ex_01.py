"""
Efetuar a leitura de dois valores numéricos inteiros representados pela variáveis A e B e
aprensentar o resultado da diferença do maior valor pelo menor.
"""

A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número interir: "))

if A > B:
    print(A - B)
else:
    print(B - A)
