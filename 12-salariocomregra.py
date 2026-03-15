import os

os.system ("cls")

print("Cálculo de aumento salarial com regra")

salario_atual = float(input("Digite o Salário atual: R$ "))

aumento1 = salario_atual * 0.15
aumento2 = salario_atual * 0.10

novo_salario1 = salario_atual + aumento1
novo_salario2 = salario_atual + aumento2

if (salario_atual <=2000):
    print(f"Novo Salário é R$: {novo_salario1:.2f}")
    print("Aumento de 15%!")

else:
    print(f"Novo Salário é: R$ {novo_salario2:.2f}")
    print("Aumento de 10%!")
