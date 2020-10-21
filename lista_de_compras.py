transacoes = 15
contador = 0
compra_total = 0
compra_parcelada = 0
compra_a_vista = 0
primeira_parcela = 0
list = []

while contador < transacoes:
    tipo_de_compra = input("A compra foi (P)arcelada ou a (V)ista?").upper()
    compra = float(input("Insira o valor da compra:"))

    compra_total += compra

    if tipo_de_compra == "P":
        compra_parcelada += compra
        compra /= 3
        list.append(compra)

    if tipo_de_compra == "V":
        compra_a_vista += compra

    contador += 1

print(f"O valor total de compras parceladas é {compra_parcelada}")
print(f"O valor total de compras à vista é {compra_a_vista}")
print(f"O valor total de todas as compras é {compra_total}")
print(f"Os valores das primeiras parcelas das compras a prazo são respectivamente:{list}")
