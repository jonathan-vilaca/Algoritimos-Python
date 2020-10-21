#3) Faça um algoritmo para ler um número inteiro e informar se o número é par ou ímpar.
print("PAR OU IMPAR")
numero = int(input("Insira um número:"))
resto = numero % 2
if resto == 0:
    print("NÚMERO É PAR!")
else:
    print("NÚMERO É IMPAR!")
