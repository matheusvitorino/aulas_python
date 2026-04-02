import os

os.system ("cls")

print("Atividade - Consumo Combustível")

km = float(input("Digite a quantidade de KM/h percorridos: "))
litros = float(input("Digite a quantidade de litros gastos: "))

consumo = km / litros

print(f"O consumo médio é: {consumo:.2f} litros")
