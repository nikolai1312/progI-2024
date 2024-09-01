"""
Exercício 04 - Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
Definir as funções eh_positivo, eh_negativo e eh_zero.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número positivo.
"""

# Solicitando número ao usuário
numero = int(input("Digite um número inteiro: "))

def eh_positivo(num: int):
    return num > -1

def eh_negativo(num: int):
    return num <= -1

def eh_zero(num: int):
    return num == 0

if(eh_positivo(numero)):
    print(f"{numero} é um número positivo.")

if(eh_negativo(numero)):
    print(f"{numero} é um número negativo.")

if(eh_zero(numero)):
    print(f"{numero} é zero.")