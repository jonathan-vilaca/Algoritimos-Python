print("TELA DE LOGIN")
login = int(input("Digite seu nome de usuário:"))
if login == 1234:
    senha = int(input("Digite sua senha:"))
    if senha == 9999:
        print("ACESSO LIBERADO!")
    else:
        print("SENHA INCORRETA!")
else:
    print("USUÁRIO INVÁLIDO!")