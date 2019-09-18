maca = int(input("Quantas maçãs você deseja?"))
if maca < 12:
    print("Valor total é R$", "{:.2f}".format(maca*1.30))
else:
    print("Valor total é R$", "{:.2f}".format(maca*1.00))