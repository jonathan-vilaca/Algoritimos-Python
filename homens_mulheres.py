homem_a = int(input("Insira a idade do homem A:"))
homem_b = int(input("Insira a idade do homem B:"))
mulher_a = int(input("Insira a idade da mulher A:"))
mulher_b = int(input("Insira a idade da mulher B:"))
if homem_a > homem_b and mulher_a > mulher_b:
    print("Idade do homem mais velho somando com a idade da mulher mais nova:", homem_a+mulher_b)
    print("O produto da idade do homem mais novo com a idade da mulher mais velha é:", homem_b*mulher_a)
if homem_a < homem_b and mulher_a < mulher_b:
    print("Idade do homem mais velho somando com a idade da mulher mais nova:", homem_b+mulher_a)
    print("O produto da idade do homem mais novo com a idade da mulher mais velha é:", homem_a*mulher_b)
if homem_a < homem_b and mulher_a > mulher_b:
    print("Idade do homem mais velho somando com a idade da mulher mais nova:", homem_b+mulher_b)
    print("O produto da idade do homem mais novo com a idade da mulher mais velha é:", homem_b*mulher_a)
if homem_a > homem_b and mulher_a < mulher_b:
    print("Idade do homem mais velho somando com a idade da mulher mais nova:", homem_a+mulher_a)
    print("O produto da idade do homem mais novo com a idade da mulher mais velha é:", homem_a*mulher_b)