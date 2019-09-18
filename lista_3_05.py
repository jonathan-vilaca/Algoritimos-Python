#5) Faça um algoritmo para ler dois números inteiros e escrever o maior.
numero1 = int(input("Insira um número:"))
numero2 = int(input("Insira um outro número:"))

numero1maiornumero2 = numero1 > numero2
numero1menornumero2 = numero1 < numero2
numero1igualnumero2 = numero1 == numero2

if numero1igualnumero2:
    print("Os números são iguais!")
if numero1maiornumero2:
    print("O número maior é:", numero1)
if numero1menornumero2:
    print("O número maior é:", numero2)