#7.Crie um algoritmo que, dado três números informados pelo usuário, verifique se algum deles é múltiplo de outro. Note que pode haver mais de um múltiplo entre eles.

print("Me dê um número natural:")
numero01 = int(input())

print("Me dê outro número natural:")
numero02 = int(input())

print("Me dê outro número natural:")
numero03 = int(input())

if (numero01 % numero02 == 0 or numero01 % numero03 == 0) and (numero02 % numero01 == 0 or numero02 % numero03 == 0):
    print(f"{numero01} é múltiplo de {numero02} ou de {numero03}.")
elif (numero02 % numero01 == 0 or numero02 % numero03 == 0) and (numero01 % numero02 == 0 or numero01 % numero03 == 0):
    print(f"{numero02} é múltiplo de {numero01} ou de {numero03}.")
elif (numero03 % numero01 == 0 or numero03 % numero02 == 0) and (numero01 % numero02 == 0 or numero01 % numero03 == 0):
    print(f"{numero03} é múltiplo de {numero01} ou de {numero02}.")
else:
    print("Nenhum número é múltiplo de outro.")
