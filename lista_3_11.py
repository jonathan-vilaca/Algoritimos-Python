#11) Faça um algoritmo para ler o nome, as três notas e o número de faltas de um aluno e
# #escrever qual a sua situação final: Aprovado, Reprovado por Falta ou Reprovado por Média.
# A média para aprovação é 7,0 e o limite de faltas é 25% do total de aulas. O número de aulas
# ministradas no semestre foi de 80. A reprovação por falta sobrepõe a reprovação por Média.
aluno = input("Insira o seu nome:")

nota1 = int(input("Insira a primeira nota:"))
nota2 = int(input("Insira a segunda nota:"))
nota3 = int(input("Insira a terceira nota:"))

faltas = int(input("Insira seu número de faltas:"))

if (nota1 + nota2 + nota3) / 3 >= 7 and faltas < 80*25/100 :
    print("APROVADO!")
else:
    if faltas >= 80*25/100:
        print("REPROVADO POR FALTA!")
    else:
        print ("REPROVADO")