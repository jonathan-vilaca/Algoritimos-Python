#9) Faça um algoritmo para ler três valores reais e informar se estes podem ou não formar os lados de um triângulo e qual tipo de triângulo seria: equilátero, isósceles ou escaleno.
print("Insira 3 valores e saiba se podem ser lados de um triãngulo e qual o tipo de triângulo:")

A = float(input("Insira o primeiro valor:"))
B = float(input("Insira o segundo valor:"))
C = float(input("Insira o terceiro valor:"))

if A == B and A != C and B != C:
    print("Com esses valores o triângulo será um isósceles!")
if B == C and A != C and A != B:
    print("Com esses valores o triângulo será um isósceles!")
if C == A and A != B and B != C:
    print("Com esses valores o triângulo será um isósceles!")
if A == B == C:
    print("Com esses valores o triângulo será um equilátero!")
if A != B and A!= C and C!=B:
    print("Com esses valores o triângulo será um escaleno!")