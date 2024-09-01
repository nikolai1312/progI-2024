"""
Exercício 07 - Escreva um programa que recebe o valor total
e aplica descontos em compras:
-5% para compras até R$100,
-10% para compras acima de R$100 até R$500, e
-15% para compras acima de R$500.
Exiba o valor original, o valor do desconto e o valor final.

Entrada:
Digite o valor total das suas compras (em R$): 200

Saída:
Valor total: R$ 200.00
Valor com desconto: R$ 180.00
Desconto: R$ 20.00
"""
def calcular_desconto(valor_total: float):
    # implemente a função
    if(valor_total > 100 and valor_total <= 500 ):
        desconto = valor_total / 10
        valor_com_desconto = valor_total - desconto
    elif(valor_total > 500):
        desconto = 15 * valor_total / 100
        valor_com_desconto = valor_total - desconto
    else:
        desconto = 5 * valor_total / 100
        valor_com_desconto = valor_total - desconto

    return desconto, valor_com_desconto

# Entrada do valor total das compras
valor_total = float(input("Digite o valor total das suas compras (em R$): "))

desconto, valor_com_desconto = calcular_desconto(valor_total)

print(f"Valor total: R$ {valor_total:.2f}")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
