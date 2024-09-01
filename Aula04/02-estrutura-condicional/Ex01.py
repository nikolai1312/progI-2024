"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.
Crie uma função chamada eh_par que recebe um número inteiro e retorna True se o número for par e False se for ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.
"""
def eh_par(numero):
    return numero % 2 == 0

num = int(input("Insira um número inteiro: "))

if(eh_par(num)):
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")
