"""
Efetuar a leitura de um valor numérico inteiro positivo ou negativo represntado pela variável N e
apresentar o valor lido como positivo.
"""

N = int(input("Digite um número positivo ou negativo: "))

if N < 0:
    print(f"O número negativo que você informou equivale +{N * -1}.")
else:
    print(f"O número que você digitou é {N}")
