kg_morango = float(input("Insira quantos kg de morango você comprou:"))
kg_maca = float(input("Insira quantos kg de maçã você comprou:"))
if kg_morango <=5:
    total_morango = kg_morango * 2.5
else:
    total_morango = kg_morango * 2.2
if kg_maca <=5:
    total_maca = kg_maca * 1.8
else:
    total_maca = kg_maca * 1.5
print("Total gasto com morangos:", "R$", "{:.2f}".format(total_morango))
print("Total gasto com maçãs:", "R$", "{:.2f}".format(total_maca))
if kg_morango + kg_maca >= 8 or total_morango+total_maca >= 25:
    print("Valor total a se pagar:", "R$", "{:.2f}".format((total_morango+total_maca)*0.90))
else:
    print("Valor total a se pagar:", "R$", "{:.2f}".format((total_morango+total_maca)))