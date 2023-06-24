"""
João Pescador, quer controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 
"""

limite_peso = 50
valor_multa_por_quilo = 4.00

peso = float(input("Digite o peso de peixes (em quilos): "))

if peso > limite_peso:
    excesso = peso - limite_peso
    multa = excesso * valor_multa_por_quilo
    print(f"Peso excedente: {excesso}Kg")
    print(f"Valor da multa a ser pago: R${multa}")
else:
    print("Não há excesso de peso. Nenhuma multa será aplicada.")
