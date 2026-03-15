import os

os.system ("cls")

print("Verificar se o número é par ou ímpar")

numero = int(input("Digite um número: "))

if (numero % 2):
    print("Número é Impar!")

else:
    print("Número é Par!")