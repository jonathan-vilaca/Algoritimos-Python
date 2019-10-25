numero = int(input("Insira um número inteiro qualquer entre 1 e 5:"))
print("Seu número...")
if numero > 5 or numero == 0 or numero < 1:
    print("Está fora do intervalo pedido!")
if numero >= 1 and numero <= 5:
    print("Está dentro do intervalo solicitado")
if numero % 2 == 0:
    print("É par")
else:
    if numero % 2 == 1:
        print("É impar")
if (numero != 1) and (numero != 4):
    print("É primo!")
