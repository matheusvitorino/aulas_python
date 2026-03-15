import os

os.system ("cls")

print("Atividade - Conversão Dollar")

dollar = float(input("Informe o valor em dollares $:  "))
cotacao_dollar = (5.33)

total = dollar * cotacao_dollar

print(f"O valor convertido em Reais é: R$ {total:.2f}")
