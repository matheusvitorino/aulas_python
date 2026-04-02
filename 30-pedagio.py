import os

os.system ("cls")

print("Atividade - Pedágio")

print("=" * 40)

carro = 1
moto = 2
caminhao =3

print("Selecione o Veículo:")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")

print("=" * 40)

veiculo = int(input("Selecione o número do veìculo: "))

if (veiculo == carro):
    valor_carro = 10.00
    print(f"Valor pedágio: R$ {valor_carro:.2f}")

elif (veiculo == moto):
    valor_moto = 5.00
    print(f"Valor pedágio: R$ {valor_moto:.2f}")

elif (veiculo == caminhao):
    valor_caminhao = 20.00
    print(f"Valor pedágio: R$ {valor_caminhao:.2f}")

else:
    print("Número inválido!")

print("=" * 40)
