pessoas = 4
contador = 0
soma_idades_f = 0
soma_idades_m = 0
total_idade = 0
idade_f = 0
idade_m = 0

while contador < pessoas:

    sexo = input("Insira seu sexo (M) ou (F):").upper()
    idade = int(input("Insira sua idade:"))

    total_idade += idade

    if sexo == "F":
        soma_idades_f += idade
        idade_f += 1

    if sexo == "M":
        soma_idades_m += idade
        idade_m += 1

    contador += 1

print(f"A média das idades dessas pessoas é:{total_idade/pessoas}")
print(f"A média das idades das mulheres é:{soma_idades_f/idade_f}")
print(f"A média das idades dos homens é:{soma_idades_m/idade_m}")
