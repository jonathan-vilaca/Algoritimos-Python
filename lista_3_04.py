#4) Faça um algoritmo para ler dois números inteiros A e B e informar se A é divisível por B.
print("Saber se A é divisível por B")
A = int(input("Insira o um número em A:"))
B = int(input("Insira o um número em B:"))

if A % B == 0:
    print("A é divisível por B!")
else:
    print("A NÃO é divisível por B!")