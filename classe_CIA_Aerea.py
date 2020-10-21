lista_cidades = ["BELO HORIZONTE", "RIO DE JANEIRO", "FORTALEZA", "SANTA CATARINA"]

class Aeroporto():

    def __init__(self):
        self.__nomeAeroporto = ["CONFINS", "PAMPULHA", "ANGRA DOS REIS"]

    def pegarNome(self):
        return self.__nomeAeroporto

    def pegarCidade(self):
        return lista_cidades

class CIA_Aerea():

    def pegarNome(self):
        return self.NomeCIA_Aerea

    def atribuirNome(self, nome):
        self.NomeCIA_Aerea = str(nome)

    def pegarCNPJ(self):
        return self.cnpj

    def atribuiCNPJ(self, cnpj):
        self.cnpj = str(cnpj)

class Cliente():

    def __init__(self):
        self.__tipo = ["VIP", "ESPECIAL", "NORMAL"]

    def gettipo(self):
        return self.__tipo

    def atribuirNome(self, nome):
        self.__nome = str(nome)

    def pegarNome(self):
        return self.__nome

    def atribuirCPF(self, cpf):
        self.__cpf = str(cpf)

    def pegarCPF(self):
        return self.__cpf

class Voo():

    def __init__(self):
        self.__codVoo = 0

    def origem(self):
        return lista_cidades

    def destino(self):
        return lista_cidades

    def getCodVoo(self):
        return self.__codVoo + 1

    def setCodVoo(self, cod):
        self.__codVoo = cod


if __name__ == "__main__":
    aeroporto = Aeroporto()
    cia = CIA_Aerea()
    cliente = Cliente()
    voo = Voo()
    cia.atribuirNome("GOL")
    cia.atribuiCNPJ("07.575.651-0001-59")
    cliente.atribuirNome("JONATHAN")
    cliente.atribuirCPF("12345678910")

    print(f"A companhia aérea {cia.pegarNome()} portadora do CNPJ: {cia.pegarCNPJ()} declara que o cliente {cliente.pegarNome()},\nTipo: {cliente.gettipo()[0]},"
          f" portador do CPF: {cliente.pegarCPF()}, possui uma passagem aérea no aeroporto da {aeroporto.pegarNome()[1]}"
          f" situado na cidade de {aeroporto.pegarCidade()[0]}")
    print("")
    print("DETALHES DO VOO")
    print("")
    print(f"Código do voo: {voo.getCodVoo()}")
    print(f"Origem: {voo.origem()[0]}")
    print(f"Destino: {voo.destino()[2]}")
