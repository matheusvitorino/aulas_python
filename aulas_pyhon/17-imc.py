import os

os.system ("cls")

print("Cáculco do IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if (imc <18.5):
    print("Abaixo do peso")
    print(f"Seu IMC é: {imc:.2f}")

elif (imc >=18.5 and (imc <=24.9)):
    print("Peso normal")
    print(f"Seu IMC é: {imc:.2f}")

else:
    print("Acima do peso")
    print(f"Seu IMC é: {imc:.2f}")