import os

os.system ("cls")

print("Atividade - Produtos")

descricao_produto = input("Informe o produto: ")
quantidade_produto = int(input("Digite a quantidade do produto: "))
preco_unitario = float(input("Digite o preço do produto: R$"))

print("=" * 40)

total = quantidade_produto * preco_unitario

print(f"O total é: R${total:.2f}")

if (quantidade_produto <=5):
    desconto = total * 2 / 100
    print(f"O preço com desconto é: R${desconto:.2f}")

elif (quantidade_produto >5 and total <=10):
    desconto = total * 3 / 100
    print(f"O preço com desconto é: R${desconto:.2f}")

else:
    desconto = total * 5 / 100
    print(f"O preço com desconto é: R${desconto:.2f}")

print("=" * 40)
