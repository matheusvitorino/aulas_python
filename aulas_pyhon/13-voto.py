import os

os.system ("cls")

print("Verificar idade para Votar")

idade = int(input("Digite sua idade: "))

if (idade >=18):
    print("Voto Obrigatório!")

elif (idade >=16 <=17):
    print("Voto Opcional!")

else:
    print("Não pode Votar!")