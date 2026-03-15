import os

os.system ("cls")

print("Atividade - Cáculo de Idade")

ano = int(input("Informe o ano: "))
ano_nascimento = int(input("Informe o ano em que a pessoa nasceu: "))

idade = ano - ano_nascimento

print(f"A pessoa tem {idade} anos")
