idade = int(input("Insira sua idade e descubra sua categoria:"))
if idade == 5 or idade == 6 or idade ==7:
    print("INFANTIL A")
else:
    if idade == 12 or idade == 13:
        print("JUVENIL A")
    else:
        if idade >= 18:
            print("ADULTO")
        else:
            print("Não poderá competir/nadar!")