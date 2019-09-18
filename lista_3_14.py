print("Atualização salarial!")
salario = float(input("Insira o seu salário:"))

if salario <= 600:
    print("Valor atualizado do seu salário é:" "R$", "{:.2f}".format(salario + salario*(30/100)))
if 600.01 < salario < 1100:
    print("Valor atualizado do seu salário é:" "R$", "{:.2f}".format(salario + salario*(25/100)))
if 1100.01 < salario < 2400:
    print("Valor atualizado do seu salário é:" "R$", "{:.2f}".format(salario + salario*(20/100)))
if 2400.01 < salario < 3550:
    print("Valor atualizado do seu salário é:" "R$", "{:.2f}".format(salario + salario*(15/100)))
if salario > 3550:
    print("Valor atualizado do seu salário é:" "R$", "{:.2f}".format(salario + salario*(10/100)))