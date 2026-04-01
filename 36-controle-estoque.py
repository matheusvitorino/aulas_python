import os

os.system ("cls")

print("Atividade - Estoque")

quantidade_produtos = int(input("Digite a quantidade de produtos em estoque: "))

if (quantidade_produtos <=5):
    print("Estoque baixo!")

else:
    print("Estoque ok!")