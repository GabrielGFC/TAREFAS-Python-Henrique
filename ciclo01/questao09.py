#9.Crie um algoritmo que, dados os lados de um triângulo informados pelo usuário, calcule a área. 

lado1 = float(input("Digite o tamanho do primeiro lado: "))
print("O tamanho do primeiro lado é:", lado1)
lado2 = float(input("Digite o tamanho do segundo lado: "))
print("O tamanho do segundo lado é:", lado2)
lado3 = float(input("Digite o tamanho do terceiro lado: "))
print("O tamanho do terceiro lado é:", lado3)

ze = (lado1 + lado2 + lado3) / 2

area = (ze * (ze - lado1) * (ze - lado2) * (ze - lado3)) ** 0.5

print("A área do triângulo é:", area)
