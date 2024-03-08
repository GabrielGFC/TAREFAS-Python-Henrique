#Crie um algoritmo que, dado três números informados pelo usuário, informe qual é o maior deles.

print("me de um número natural :")

numero01 = int(input())

print("me de outro número natural:")

numero02 = int(input())

print("me de outro número natural:")

numero03 = int(input())

if numero01 > numero02 and numero01 > numero03:
    print("O número", numero01, "é o maior.")
elif numero02 > numero01 and numero02 > numero03:
    print("O número", numero02, "é o maior.")
elif numero03 > numero01 and numero03 > numero02:
    print("O número", numero03, "é o maior.")
else:
    print("Os números são iguais.")
1
