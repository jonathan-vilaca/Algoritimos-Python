print("Qual a área deseja calcular?")
figura = int(input("Digite 1 para Triangulo, 2 para Quadrado e 3 para Círculo:"))
if figura == 1:
    altura_triangulo = int(input("Insira o valor da altura do triangulo:"))
    base_triangulo = int(input("Insira o valor da base do triangulo:"))
    print("O valor da área do triangulo é", (altura_triangulo*base_triangulo)/2)
if figura == 2:
    lado_quadrado = int(input("Insira o valor do lado do quadrado:"))
    print("O valor da área do quadrado é:", lado_quadrado*lado_quadrado)
if figura == 3:
    raio_circ = float(input("Insira o valor do raio do círculo:"))
    print("O valor da área do área é:", 3.14*(raio_circ*raio_circ))