#10) Faça um algoritmo para ler três números positivos e escrevê-los em ordem crescente.
print("Digite 3 números para vê-los em ordem crescente:")
numero1 = int(input("Insira o primeiro número:"))
numero2 = int(input("Insira o segundo número:"))
numero3 = int(input("Insira o terceiro número:"))
if numero1 > numero2 > numero3:
    print("A ordem crescente é:", numero3, numero2, numero1)
if numero1 > numero3 > numero2:
    print("A ordem crescente é:", numero2, numero3, numero1)
if numero2 > numero3 > numero1:
    print("A ordem crescente é:", numero1, numero3, numero2)
if numero2 > numero1 > numero3:
    print("A ordem crescente é:", numero3, numero1, numero2)
if numero3 > numero1 > numero2:
    print("A ordem crescente é:", numero2, numero1, numero3)
if numero3 > numero2 > numero1:
    print("A ordem crescente é:", numero1, numero2, numero3)