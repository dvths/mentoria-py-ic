"""
Realizar a leitura de dos valores de quatro notas escolares bimestrais de um aluno representadas
pelas variváveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e aprensetar a
mensagem "Aprovado" se a média for maior ou igual a 5; caso contrário, apresentar a mensagem
"Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
"""

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

MD = (N1 + N2 + N3 + N4) / 4

if MD >= 5:
    print("Aprovado")
    print(f"Sua média foi ---> {MD}")
else:
    print("Reprovado")
    print(f"Sua média foi ---> {MD}")
