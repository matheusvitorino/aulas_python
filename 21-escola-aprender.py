import os

os.system ("cls")

print("Atividade - Escola Aprender")

nivel = int(input("Informe qual o seu nível (1,2 ou 3): "))
quantidade_aula = int(input("Informe qual a quantidade de aulas por semana: "))

if nivel == 1:
    valor_hora = 12.00

elif nivel == 2:
    valor_hora = 17.00

elif nivel == 3:
    valor_hora = 25.00

else:
    print("Nível inválido!")
    exit()

salario = valor_hora * quantidade_aula * 4

print(f"Salário mensal é: {salario:.2f}")
