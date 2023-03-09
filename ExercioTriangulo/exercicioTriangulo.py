lateral1 = int(input("Digite o tamanho da lateral do triangulo: "))
lateral2 = int(input("Digite o tamanho da segunda lateral do triangulo: "))
base = int(input("Digite o tamanho da base do triangulo: "))
altura = int(input("Digite a altura do triangulo: "))
perimetro = lateral1 + lateral2 + base
area = base * altura / 2

print(f"O perimetro desse triangulo é: {perimetro}")
print(f"A area desse triangulo é: {area}")