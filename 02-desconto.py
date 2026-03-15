import os

os.system ("cls")

print("Calculadora de Desconto")
nome_produto = input("Entre com o nome do Produto: ")
preco = float(input("Entre com o valor do Produto: "))
percentual_desconto = float(input("Entre com o porcentual de Desconto %: "))

valor_desconto = preco * percentual_desconto / 100
preco_final = preco - valor_desconto

print("===========================================================")
print("Preço original: ", preco , "Preço com desconto: ", preco_final)
print(f"Preço original: R$ {preco} - Preço com desconto: R$ {preco_final}")