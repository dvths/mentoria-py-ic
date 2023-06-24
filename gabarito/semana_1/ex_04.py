"""
Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1,
N2, N3, N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem "Aprovado
se a média obtida for maior ou igual a 7; caso contrário, o programa deve solicitar a quinta nota
(nota de exame, representada pela variável NE) do aluno e calcular uma nova média aritmética
(variável MD2) entre a nota de exame e a primeira média aritmética. Se o valor da média for maior ou
igual a 5, apresentar a mensagem "Aprovado em exame"; caso contrário, apresentar a menagem
"Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
"""

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

MD = round((N1 + N2 + N3 + N4) / 4, 2)

if MD >= 7:
    print("Aprovado")
    print(f"Sua média foi ---> {MD}")
else:
    print(f"Sua média foi ---> {MD}")
    NE = float(input("Digite a nota de exame: "))
    MD2 = round((NE + MD) / 2, 2)

    if MD2 >= 5:
        print("Aprovado em exame ")
        print(f"Sua média final foi ---> {MD2}")
    else:
        print("Reprovado")
        print(f"Sua média final foi ---> {MD2}")
