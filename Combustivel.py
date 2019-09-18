print("Calcule quanto gastará com combustível")

tipo = input("Insira o tipo de combustível gasolina(G) ou alcool(A):")

litros = float(input("Insira quantos litros de combustível você colocou:"))

#valor da gasolina por litro
alcool = float(2.90)
#valor do alcool por litro
if tipo.upper() == "G":
    if litros <= 20:
        print("Valor total a ser pago:", "{:.2f}".format(3.3*0.96*litros))
    else:
        print("Valor total a ser pago:", "{:.2f}".format(3.3*0.94*litros))
if tipo.upper() == "A":
    if litros <= 20:
        print("Valor total a ser pago:", "{:.2f}".format(alcool*0.97*litros))
    else:
        print("Valor total a ser pago:", "{:.2f}".format(alcool*0.95*litros))