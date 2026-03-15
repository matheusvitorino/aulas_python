import os

os.system ("cls")

print("Atividade - Habilitação")

idade = int(input("Digite sua idade: "))

if (idade >=18):
    habilitacao = input("Possui habilitação (Sim) ou (Não): ")

    if habilitacao == "Sim":
        print("O Usuário pode dirigir!")

    elif habilitacao == "Não":
        print("O usuário não pode dirigir!")

else:
    print("O usuário não pode dirigir!")