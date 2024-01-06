class Endereco:

    def __init__(self, salao, cidade, cep, rua, bairro, numero, contato):
        self.salao = salao
        self.cidade = cidade
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.contato = contato
        
    # Método para imprimir informações do salão
    def informacoesDoSalao(self):
        print (f'Salão {self.salao}\n{self.cidade} | {self.cep}\nRua: {self.rua}, Bairro:{self.bairro}, Nº {self.numero }\nContato:{self.contato}')


#instância de Endereco
salao1 = Endereco("Beleza Vip", "Portalegre/RN", "5981000", "Antonio Epifanio", "centro", "20", 98202268)
salao1.informacoesDoSalao()



