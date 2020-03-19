print("Calcule quantos dias de vida vc tem:")
ano = int(input("Digite quantos anos você tem: "))
mes = int(input("E os meses? "))
dia = int(input("E dias? "))
idade_em_dias = (ano*365) + (mes*30) + dia
print(f"Você possui {idade_em_dias} dias de vida")
