#7) Faça um algoritmo para ler os coeficiente de uma equação do segundo grau e calcular as suas raízes, na forma Ax² + Bx + C, levando em consideração a existência de raízes reais (Δ > 0, a equação possui duas raízes reais e distintas; Δ = 0, a equação possui raízes reais iguais; Δ < 0, a equação não possui raízes reais).
import math
print("Sabendo que uma equação do segundo grau possui a forma Ax²+Bx+C, indique suas variáveis para calcular seu coeficiente:")
A = float(input("Insira o valor de A:"))
B = float(input("Insira o valor de B:"))
C = float(input("Insira o valor de C:"))

delta = B**2 - 4 * A * C
x1 = ((-1*B) + math.sqrt(delta)) / (2 * A)
x2 = ((-1*B) - math.sqrt(delta)) / (2 * A)

print("Valor de Delta:", delta)
print("Valor da raíz x¹:", x1)
print("Valor da raíz x²:", x2)

if delta > 0:
    print("Raízes reais distintas!")
if delta < 0:
    print("Equação não possui raízes reais!")
if delta == 0:
    print("Equação possui raízes reais iguais!")