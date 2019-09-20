idade1 = int(input("Insira a idade da pessoa 1:"))
peso1 = float(input("Insira a peso da pessoa 1:"))
altura1 = float(input("Insira a altura da pessoa 1:"))

idade2 = int(input("Insira a idade da pessoa 2:"))
peso2 = float(input("Insira a peso da pessoa 2:"))
altura2 = float(input("Insira a altura da pessoa 2:"))

idade3 = int(input("Insira a idade da pessoa 3:"))
peso3 = float(input("Insira a peso da pessoa 3:"))
altura3 = float(input("Insira a altura da pessoa 3:"))

#Média das idades das pessoas acima de 20 anos.

if idade1 > 20 and idade2 > 20 and idade3 > 20:
    print("A média de idades acima de 20 anos é:", (idade1+idade2+idade3)/3)
else:
    if idade1 > 20 and idade2 > 20 and idade3 < 20:
        print("A média de idades acima de 20 anos é:", (idade1+idade2)/2)
    else:
        if idade1 > 20 and idade2 < 20 and idade3 < 20:
            print("A média de idades acima de 20 anos é:", idade1)
        else:
            if idade1 > 20 and idade2 < 20 and idade3 > 20:
                print("A média de idades acima de 20 anos é:", (idade1+idade3)/2)
            else:
                if idade1 < 20 and idade2 > 20 and idade3 > 20:
                    print("A média de idades acima de 20 anos é:", (idade2+idade3)/2)
                else:
                    if idade1 < 20 and idade2 < 20 and idade3 > 20:
                        print("A média de idades acima de 20 anos é:", idade3)
                    else:
                        if idade1 < 20 and idade2 > 20 and idade3 < 20:
                            print("A média de idades acima de 20 anos é:", idade2)
                        else:
                            print("Nenhuma pessoa possue idade maior que 20 anos.")

#Média das alturas das pessoas  entre 15 e 18 anos.

if (idade1 >= 15 and idade1 <= 18) and (idade2 >= 15 and idade2 <= 18) and (idade3 >= 15 and idade3 <= 18):
    print("A média das alturas entre 15 e 18 é:", (altura1 + altura2 + altura3)/3)
else:
    if (idade1 < 15 or idade1 > 18) and (idade2 >= 15 and idade2 <= 18) and (idade3 >= 15 and idade3 <= 18):
        print("A média das alturas entre 15 e 18 é:", (altura2 + altura3)/2)
    else:
        if (idade1 >= 15 and idade1 <= 18) and (idade2 < 15 or idade2 > 18) and (idade3 >= 15 and idade3 <= 18):
            print("A média das alturas entre 15 e 18 é:", (altura1 + altura3)/2)
        else:
            if (idade1 >= 15 and idade1 <= 18) and (idade2 >= 15 and idade2 <= 18) and (idade3 < 15 or idade3 > 18):
                print("A média das alturas entre 15 e 18 é:", (altura1 + altura2)/2)
            else:
                if (idade1 >= 15 and idade1 <= 18) and (idade2 < 15 or idade2 > 18) and (idade3 < 15 or idade3 > 18):
                    print("A média das alturas entre 15 e 18 é:", altura1)
                else:
                    if (idade1 < 15 or idade1 > 18) and (idade2 >= 15 and idade2 <= 18) and (idade3 < 15 or idade3 > 18):
                        print("A média das alturas entre 15 e 18 é:", altura2)
                    else:
                        if (idade1 < 15 or idade1 > 18) and (idade2 < 15 or idade2 > 18) and (idade3 >= 15 and idade3 <= 18):
                            print("A média das alturas entre 15 e 18 é:", altura3)
                        else:
                            print("Não há pessoas entre 15 e 18 anos!")

#Porcentagem de pessoas abaixo de 60kg.

if peso1 <= 60 and peso2 <= 60 and peso3 <= 60:
    print("A porcentagem de pessoas abaixo de 60kg é 100% ")
else:
    if (peso1 <= 60 and peso2 > 60 and peso3 <= 60) or (peso1 <= 60 and peso2 <= 60 and peso3 > 60) or (peso1 > 60 and peso2 <= 60 and peso3 <= 60):
        print("A porcentagem de pessoas abaixo de 60kg é 66%")
    else:
        if (peso1 > 60) or (peso2 > 60) or (peso3 > 60):
            print("A porcentagem de pessoas abaixo de 60kg é 33%")
        else:
            print("A porcentagem de pessoas abaixo de 60kg é 0%")
