#6) Faça um algoritmo para ler duas variáveis inteiras A e B e garantir que A e B fiquem em
# ordem crescente, ou seja, a variável deverá armazenar o menor valor fornecido e a variável B o maior.
print("Coloque em ordem crescente:")
A = int(input("Insira o primeiro número:"))
B = int(input("Insira o segundo número:"))

if A > B:
    print("A ordem crescente é B e A")
else:
    print("A ordem crescente é A e B")