#8. Crie um algoritmo que, dados o tamanho de três lados informados pelo usuário, verifique se: (1) é um triângulo isósceles, (2) é equilátero, (3) é escaleno ou (4) não é um triângulo.

lado01 = float(input("Digite o tamanho do primeiro lado: "))
print("O tamanho do primeiro lado é:", lado01)
lado02 = float(input("Digite o tamanho do segundo lado: "))
print("O tamanho do segundo lado é:", lado02)
lado03 = float(input("Digite o tamanho do terceiro lado: "))
print("O tamanho do terceiro lado é:", lado03)

if lado01 + lado02 > lado03 and lado01 + lado03 > lado02 and lado02 + lado03 > lado01:
    if lado01 == lado02 == lado03:
        print("É um triângulo equilátero.")
    elif lado01 == lado02 or lado01 == lado03 or lado02 == lado03:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")
