#5.Agora altere o algoritmo anterior de maneira que ele verifique também se o nível informado está entre 0 e 10. Caso contrário uma mensagem de erro deve ser apresenta. 

print("Digite o nível de alerta de risco (um número de 0 a 10): ")
nivel_alerta = int(input())

if nivel_alerta >= 0 and nivel_alerta <= 10:
    if nivel_alerta <= 3:
        print("O nível de alerta é BAIXO.")
    elif nivel_alerta <= 6:
        print("O nível de alerta é MÉDIO.")
    elif nivel_alerta <= 9:
        print("O nível de alerta é ALTO.")
    else:
        print("O nível de alerta é GRAVE.")
else:
    print("Erro: O nível de alerta deve estar entre 0 e 10.")
