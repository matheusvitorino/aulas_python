import os

os.system ("cls")

print("Seja Bem vindo ao boletim virtual!")

nota01 = float(input("Entre com a primeira nota: "))
nota02 = float(input("Entre com a segunda nota: "))
nota03 = float(input("Entre com a terceira nota: "))

media = (nota01 + nota02 + nota03) / 3

if(media >= 6):
    print("Você foi Aprovado!")

elif(media >= 4 and media <=5):
    print("Você está de Recuperação!")

else:   
   print("Você foi Reprovado!")     

print(f"Sua média foi {media}")
