#8) Elabore um algoritmo para testar se uma senha digita é igual a “batatafrita”. Se a senha estiver correta escreva “Acesso permitido”, do contrário emita a mensagem “Você não tem acesso ao sistema”.
senha = input("Insira sua senha:")
if senha == "batatafrita":
    print("Acesso permitido!")
else:
    print("Você não tem acesso ao sistema!")