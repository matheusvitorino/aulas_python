import os

os.system ("cls")

print("Cálculo do salário com aumento")

salario = float(input("Informe qual o salário: "))
aumento = salario * 0.10

novo_salario = salario + aumento

print(f"O novo Salário é: R$ {novo_salario:.2f}")