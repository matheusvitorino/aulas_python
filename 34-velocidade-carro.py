import os

os.system ("cls")

print("Atividade - Velocidade Carro")

velocidade_carro = float(input("Digite a velocidade do veículo em Km/h: "))

if velocidade_carro >=80.0:
    print("Multado!")

else:
    print("Dentro do limite!")