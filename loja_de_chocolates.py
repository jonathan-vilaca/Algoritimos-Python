'''
A empresa de chocolates Interior Cacau, necessita de um controle de vendas diário para
sua loja em um famoso shopping da região. Você foi solicitado a desenvolver um
sistema básico para atender as seguintes necessidades:
a. Cadastro de clientes
b. Cadastro de funcionários
c. Cadastro de produtos
d. Cadastro de formas de pagamento
e. Registro de Vendas
f. Relatório de Vendas no dia
i. Fluxo de caixa: soma dos valores em crédito, débito e dinheiro
ii. Soma por funcionário
iii. Soma por produto
'''

#Registro de funcionários e clientes cadastrados
clientes = []
funcionarios = []

#Registro de produtos
lista_produtos = []
valor_produto = []

#Valores de compras realizadas separadas por tipos de pagamento
vendido_credito = []
vendido_debito = []
vendido_dinheiro = []

#Registro por compras

venda_por_vendedor = []


def reset():
    resposta = input("Você deseja mais alguma coisa? (S) ou (N) ")
    if resposta.upper() == "S":
        menu()
    elif resposta.upper() == "N":
        print("Ok, até a próxima! 👋")
    else:
        print("Favor inserir uma resposta válida! (S) ou (N) ")
        reset()


def cadastro(tipo, nomes):
    if tipo == "1":
        clientes.append(nomes)
        reset()
    elif tipo == "2":
        funcionarios.append(nomes)
        reset()
    elif tipo == "3":
        lista_produtos.append(nomes)
        preco = float(input("Insira o valor do produto: "))
        valor_produto.append(preco)
        reset()


def tipo_venda(tipo, valor):
    if tipo == '1':
        vendido_credito.append(valor)
    elif tipo == "2":
        vendido_debito.append(valor)
    elif tipo == "3":
        vendido_dinheiro.append(valor)
    else:
        print("Favor inserir uma entrada válida!")
        tipo_venda()


def venda():
    produto = input("O que deseja comprar? ")
    quantidade = int(input("Quantos?"))
    if produto in lista_produtos:
        print(f"O valor unitário do {produto} é {valor_produto[lista_produtos.index(produto)]}, total a pagar: {valor_produto[lista_produtos.index(produto)]*quantidade}")
        print("1 - CRÉDITO | 2 - DÉBITO | 3 - DINHEIRO")
        pagamento = input("Qual o tipo de pagamento: ")
        tipo_venda(pagamento, valor_produto[lista_produtos.index(produto)]*quantidade)
        cod_vendedor = input("Insira o código do vendedor: ")
        venda_por_vendedor.append(cod_vendedor)
        print("Compra realizada com sucesso!")
        reset()
    else:
        print("Não existe o produto em estoque!")
        reset()


def relatorio():
    print("")
    print(20*'~~')
    print("RELATÓRIO COMPLETO DA INTERIOR CACAU")
    print(20*'~~')
    print("")
    print(f"O total em vendas no crédito foram: R$ {sum(vendido_credito)}")
    print(f"O total em vendas no débito foram: R$ {sum(vendido_debito)}")
    print(f"O total em vendas no dinheiro foram: R$ {sum(vendido_dinheiro)}")
    print(venda_por_vendedor)

def menu():
    print("O que deseja fazer?")
    print("")
    print("1 - CADASTRAR CLIENTE | 2 - CADASTRAR FUNCIONÁRIOS | 3 - CADASTRAR PRODUTOS | 4 - VENDA | 5 - RELATÓRIOS "
          "FINAIS")
    tipo_cadastro = input("")

    if tipo_cadastro == "1" or tipo_cadastro == "2" or tipo_cadastro == "3":
        nome = input("Insira o nome ou código: ")
        cadastro(tipo_cadastro, nome)
    elif tipo_cadastro == "4":
        venda()
    elif tipo_cadastro == "5":
        relatorio()

    else:
        print("Favor inserir uma entrada válida!")
        print("")
        menu()

print(15 * "~~")
print("BEM VINDO A INTERIOR CACAU")
print(15 * "~~")
print("")
menu()
