print("CALCULADORA")
numero_a = float(input("Insira um numero: "))
sinal = input("Insira o sinal da operacao: ")
numero_b = float(input("Insira o segundo numero: "))

if (sinal != "+") and (sinal != "-") and (sinal != "*") and (sinal != "/"):
    print("Insira apenas sinais de operação básica")

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
