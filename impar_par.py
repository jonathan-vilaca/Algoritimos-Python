numero = int(input("Digite um número para saber se é Par(P) ou Impar(I):"))
resto = numero % 2
if resto == 0:
    Par = numero
    Impar = None
else:
    Par = None
    Impar = numero
print("P:", Par)
print("I:", Impar)