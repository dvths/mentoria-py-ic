"""
Vamos supor que a câmara de deputados, legislando em causa própria, resolveu aumentar o salário e as
verbas dos seus integrantes (o que seria absolutamente imoral!) e vc está investigando essa decisão
calculando os reajustes. 

Faça um programa que recebe o salário de um deputado e o reajuste segundo o seguinte critério, baseado no salário atual:

    Cota para exercício de Atividade Parlamentar (salário) entre R$30.800,00 e R$40.500,00: aumento de 20%
    Verba de Contratação de Pessoal de R$106.866,59: aumento de 15%
    Auxílio Moradia de R$4.253 : aumento de 20%

Após o aumento ser realizado, apresente:
    - salário antes do reajuste;
    - percentual de aumento aplicado;
    - valor do aumento;
    - novo salário, após o aumento
"""

salario_atual = float(input("Digite o salário atual do deputado: "))

salario_antigo = salario_atual

# Reajuste para Cota para exercício de Atividade Parlamentar
if 30800 <= salario_atual <= 40500:
    percentual_aumento = 20
    aumento = salario_atual * 0.2
    salario_atual += aumento

# Reajuste para Verba de Contratação de Pessoal
elif salario_atual == 106866.59:
    percentual_aumento = 15
    aumento = salario_atual * 0.15
    salario_atual += aumento

# Reajuste para Auxílio Moradia
elif salario_atual == 4253:
    percentual_aumento = 20
    aumento = salario_atual * 0.2
    salario_atual += aumento

else:
    percentual_aumento = 0
    aumento = 0

print("Salário antes do reajuste: R$", salario_antigo)
print("Percentual de aumento aplicado: ", percentual_aumento, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário após o aumento: R$", salario_atual)
