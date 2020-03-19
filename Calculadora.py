print("CALCULADORA")
numero_a = int(input("Insira um numero: "))
sinal = input("Insira o sinal da operacao: ")
numero_b = int(input("Insira o segundo numero: "))
if sinal == "+":
    print("Resultado é:", numero_a + numero_b)    
else:
    if sinal == "-":
        print("Resultado é:", numero_a - numero_b)
    else:
        if sinal == "*":
            print("Resultado é:", numero_a * numero_b)
        else:
            if sinal == "/":
                print("Resultado é:", numero_a / numero_b)
if (sinal != "+") and (sinal != "-") and (sinal = "*") and (sinal != "/"):
    print("Insira apenas sinais de operação básica")
