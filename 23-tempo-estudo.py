import os

os.system ("cls")

print("Atividade - Tempo de Estudo")

tempo_estudo = int(input("Digite a quantidade de estudo diária do usuário em horas: "))

if tempo_estudo <=2.0:
    print("Pouco estudo!")

elif tempo_estudo >2.0 and tempo_estudo <=4.0:
    print("Estudo médio!")

else:
    print("Muito estudo!")
