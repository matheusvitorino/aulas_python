import os

os.system("cls")

print("Atividade - Semáforo")

cor_semaforo = input("Informe a cor do semáforo: ").lower()
cor1 = "verde"
cor2 = "amarelo"
cor3 = "vermelho"

if cor_semaforo == cor1:
    print("Pode passar!")

elif cor_semaforo == cor2:
    print("Atenção!")

elif cor_semaforo == cor3:
    print("Pare!")

else:
    print("Cor inválida")