#10. Considerando o sistema de notas da UniEVANGÉLICA, construa um algoritmo que, dadas 4 notasparciais de um aluno pelo usuário, calcule a média e imprima se o aluno foi aprovado ou reprovado.Considere os 3 ciclos.

nota1 = float(input("Digite a primeira nota parcial: "))
print("A primeira nota parcial é:", nota1)
nota2 = float(input("Digite a segunda nota parcial: "))
print("A segunda nota parcial é:", nota2)
nota3 = float(input("Digite a terceira nota parcial: "))
print("A terceira nota parcial é:", nota3)
nota4 = float(input("Digite a quarta nota parcial: "))
print("A quarta nota parcial é:", nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print("O aluno foi aprovado com média:", media)
else:
    print("O aluno foi reprovado com média:", media)
