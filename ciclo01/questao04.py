#4.Crie um algoritmo que, dado o nível de alerta de risco, imprima se ele for GRAVE. O nível de alerta é um número que varia de 0 a 10. O nível é considerado GRAVE quando ele é superior a 9. 

nivel_alerta = int(input("Digite o nível de alerta de risco (um número de 0 a 10): "))


if nivel_alerta > 9:
    print("O nível de alerta é GRAVE.")
else:
    print("O nível de alerta não é considerado GRAVE.")