# 11. Agora altere o algoritmo anterior de maneira que ele permita que o professor, antes de informar as notas,informe os seus respectivos pesos. Depois disso o algoritmo deve, de análoga ao exercício anterior,calcular a média, no entanto, agora considerando os seus pesos. Lembrete: A soma dos pesos das notas sempre deve ser 10. 

peso1 = float(input("Digite o peso da primeira nota: "))
print("O peso da primeira nota é:", peso1)
peso2 = float(input("Digite o peso da segunda nota: "))
print("O peso da segunda nota é:", peso2)
peso3 = float(input("Digite o peso da terceira nota: "))
print("O peso da terceira nota é:", peso3)
peso4 = float(input("Digite o peso da quarta nota: "))
print("O peso da quarta nota é:", peso4)

soma_pesos = peso1 + peso2 + peso3 + peso4
if soma_pesos != 10:
    print("Erro: A soma dos pesos das notas deve ser igual a 10.")
else:
    nota1 = float(input("Digite a primeira nota parcial: "))
    nota2 = float(input("Digite a segunda nota parcial: "))
    nota3 = float(input("Digite a terceira nota parcial: "))
    nota4 = float(input("Digite a quarta nota parcial: "))

    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / 10

    if media_ponderada >= 7.0:
        print("O aluno foi aprovado com média:", media_ponderada)
    else:
        print("O aluno foi reprovado com média:", media_ponderada)
