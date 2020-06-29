livros_disponiveis = []
livros_emprestados = []
usuarios = []
bibliotecarios = []

print(30 * '-')
print("BIBLIOTECA EPSA")
print(30 * '-')
print("")


def opcoes():
    print("")
    print("O que faremos agora?")
    print("")
    print("Cadastro de usuário? Digite 1")
    print("Cadastro de livros novos? Digite 2")
    print("Cadastro de novos bibliotecários? Digite 3")
    print("Empréstimos de livros? Digite 4")
    print("Devolução de livros? Digite 5")
    print("Relatório de livros emprestasdos e disponíveis? Digite 6")
    print("")

opcoes()


def reinicio():
    resposta = input("Deseja mais alguma coisa? (S) ou (N) ")
    if resposta.upper() == 'S':
        opcoes()
        servico()
    elif resposta.upper() == 'N':
        print("Ok, até a próxima! 👋")
    else:
        print("Favor inserir uma entrada válida! (S) ou (N)")
        print("")
        reinicio()


def usuario():
    novo_usuario = input("Insira o nome do novo usuário: ")
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")
    print(f'Os usuários cadastrados são: {usuarios}')
    reinicio()


def livros():
    novo_livro = input("Insira o nome do novo livro: ")
    livros_disponiveis.append(novo_livro)
    print("Livro cadastrado com sucesso!")
    reinicio()


def novos_bibliotecarios():
    novo_biblio = input("Insira o nome do novo bibliotecário: ")
    bibliotecarios.append(novo_biblio)
    print("Bibliotecário cadastrado com sucesso!")
    reinicio()


def emprestimo_livro():
    emprestimo = input("Qual livro será emprestado? ")
    if emprestimo in livros_disponiveis:
        livros_disponiveis.remove(emprestimo)
        livros_emprestados.append(emprestimo)
        reinicio()
    elif emprestimo in livros_emprestados:
        print("Livro se encontra emprestado!")
        reinicio()
    else:
        print("Livro não se encontra no acervo!")
        reinicio()

def devolucao_de_livros():
    devolucao = input("Qual livro será devolvido? ")
    if devolucao in livros_emprestados:
        livros_emprestados.remove(devolucao)
        livros_disponiveis.append(devolucao)
        reinicio()
    else:
        print("Este livro não pertence a esta biblioteca!")
        reinicio()


def relatorio_completo():
    print(f'Os livros de nosso acervo são:')
    print("")
    print(f"{livros_disponiveis} estão disponíveis para empréstimo")
    print("")
    print(f"E estes: {livros_emprestados}, não estão disponíveis para empréstimos pois já estão emprestados.")
    reinicio()


def servico():
    tipo_de_servico = input("O que vc deseja? ")
    if tipo_de_servico == '1':
        usuario()
    elif tipo_de_servico == '2':
        livros()
    elif tipo_de_servico == '3':
        novos_bibliotecarios()
    elif tipo_de_servico == '4':
        emprestimo_livro()
    elif tipo_de_servico == '5':
        devolucao_de_livros()
    elif tipo_de_servico == '6':
        relatorio_completo()
    else:
        print("Favor inserir uma entrada válida! De 1 a 6")
        servico()

servico()
