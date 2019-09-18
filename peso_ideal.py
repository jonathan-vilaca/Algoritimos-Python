print("Calcule seu peso ideal")
altura = float(input("Insira sua altura: "))
sexo = input("Insira seu sexo(M ou F em maiúsculos):")
if sexo == "M":
   print("{:.2f}".format((72.7*altura)-58), "Kg")
else:
   print("{:.2f}".format((62.1*altura)-44.7), "Kg")
