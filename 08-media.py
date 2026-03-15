import os

os.system ("cls")

print("Cálculo da média de duas notas")

nota01 = int(input("Entre com a primeira nota: "))
nota02 = int(input("Entre com a segunda nota: "))

media = (nota01 + nota02) /2

print(f"Sua média final é: {media}")

if (media >=6):
    print("O Aluno foi Aprovado!")

elif (media >=5 <6):
    print("O Aluno está de Recuperação!")

else:
    print("O Aluno foi Reprovado!")
    