"""
Efetuar a leitura de três valores numéricos (representados pelas variáveis A, B e C) e processar o
cálculo da equação completa de segundo grau, utilizando a fórmula de Bhaskara (considerar para a
solução do problema todas as possíveis condições para delta: delta < 0 - não há solução real, 
delta > 0 - há duas soluções reais e diferentes e delta = 0 há apenas uma solução real). Lembre-se
que é completa a equação de segundo grau que possui todos os coeficientes A, B e C diferentes de
zero. O programa deve apresentar as respostas para todas as condições estabelecidas para delta.
"""

import math

A = float(input("Digite o valor do coeficiente A: "))
B = float(input("Digite o valor do coeficiente B: "))
C = float(input("Digite o valor do coeficiente C: "))

delta = B**2 - 4 * A * C

if delta < 0:
    print("Não há solução real.")
elif delta > 0:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    print("Há duas soluções reais diferentes:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
else:
    x = -B / (2 * A)
    print("Há apenas uma solução real:")
    print(f"x = {x}")
