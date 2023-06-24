"""
Ler três valores inteiros representados pelas variáveis A, B e C e apresentar os valores dispostos
em ordem crescente. 
"""

A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número inteiro: "))
C = int(input("Digite o terceiro número inteiro: "))

if A <= B and A <= C:
    menor = A
    if B <= C:
        meio = B
        maior = C
    else:
        meio = C
        maior = B
elif B <= A and B <= C:
    menor = B
    if A <= C:
        meio = A
        maior = C
    else:
        meio = C
        maior = A
else:
    menor = C
    if A <= B:
        meio = A
        maior = B
    else:
        meio = B
        maior = A

print(f"Valores em ordem crescente: {menor}, {meio}, {maior}")


# Alternativa:
# A = int(input("Digite o valor de A: "))
# B = int(input("Digite o valor de B: "))
# C = int(input("Digite o valor de C: "))

# menor = min(A, B, C)
# maior = max(A, B, C)
# meio = (A + B + C) - menor - maior

# print(f"Valores em ordem crescente: {menor}, {meio}, {maior}")
