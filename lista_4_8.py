jogador1 = input("jogador 1, Escolha entre par ou impar:").lower().strip()

if jogador1 not in ('par', 'impar', 'ímpar'):
    print("Favor escolher PAR ou IMPAR")
else:
    if jogador1 == "par":
        jogador2 = "impar"

    if jogador1 == "impar":
        jogador2 = "par"

    jogador1_numero = int(input("Agora insira um número inteiro qualquer:"))
    jogador2_numero = int(input("Jogador 2, insira um número inteiro qualquer:"))

    if (jogador1 == "par") and ((jogador1_numero+jogador2_numero) % 2 == 0):
        print("Jogardor 1 ganhou!")
    else:
        if (jogador1 == "impar") and ((jogador1_numero+jogador2_numero) % 2 == 1):
            print("Jogardor 1 ganhou!")
        else:
            if (jogador2 == "par") and ((jogador1_numero+jogador2_numero) % 2 == 0):
                print("Jogardor 2 ganhou!")
            else:
                if (jogador2 == "impar") and ((jogador1_numero+jogador2_numero) % 2 == 1):
                    print("Jogardor 2 ganhou!")