print("Classificação etária para filmes.")
nome = input("Insira seu nome:")
idade = int(input("Insira sua idade:"))

if idade <= 10:
    print("Você não poderá assistir filmes que são proibidos para menores de 10 anos!")
if idade <= 12 and idade > 10:
    print("Você não poderá assistir filmes que são proibidos para menores de 12 anos!")
if idade <= 14 and idade > 12:
    print("Você não poderá assistir filmes que são proibidos para menores de 14 anos!")
if idade <= 16 and idade > 14:
    print("Você não poderá assistir filmes que são proibidos para menores de 16 anos!")
if idade < 18 and idade > 16:
    print("Você não poderá assistir filmes que são proibidos para menores de 18 anos!")
if idade >= 18:
    print("Você poderá assistir qualquer filme!")