"""
Ler cinco valores numéricos inteiros (variáveis A, B, C, D e E), identificar e apresentar o maior e
o menor valores informados. Não execute ordenação dos valores como no exercício anterior.
"""

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
E = int(input("Digite o valor de E: "))

maior = A
menor = A

if B > maior:
    maior = B
elif B < menor:
    menor = B

if C > maior:
    maior = C
elif C < menor:
    menor = C

if D > maior:
    maior = D
elif D < menor:
    menor = D

if E > maior:
    maior = E
elif E < menor:
    menor = E

print("Maior valor:", maior)
print("Menor valor:", menor)
