from abc import ABC, abstractmethod

class Servico(ABC):
    @abstractmethod
    def calcular_valor(self):
        raise NotImplementedError("Método calcular_valor deve ser implementado nas classes filhas.")
    
class ServicoCabelo(Servico):
    def _init_(self, tamanho_cabelo):
        self.taxa = self._calcular_taxa(tamanho_cabelo)

    def _calcular_taxa(self, tamanho_cabelo):
        if tamanho_cabelo == 'curto':
            return 0.5
        elif tamanho_cabelo == 'medio':
            return 0.8
        elif tamanho_cabelo == 'longo':
            return 1.15
        else:
            raise ValueError("Tamanho de cabelo inválido")

    def calcular_valor(self, opcao_cabelo):
        if opcao_cabelo == '1':
            return self.taxa * 100 + 100
        elif opcao_cabelo == '2':
            return self.taxa * 50 + 50
        elif opcao_cabelo == '3':
            return self.taxa * 80 + 80
        elif opcao_cabelo == '4':
            return self.taxa * 40 + 40
        elif opcao_cabelo == '5':
            return self.taxa * 70 + 70
        elif opcao_cabelo == '6':
            return self.taxa * 60 + 60
        else:
            raise ValueError("Opção de cabelo inválida")

class ServicoUnha(Servico):
    def calcular_valor(self, tipo_unha):
        if tipo_unha == '7':
            return 80
        elif tipo_unha == '8':
            return 65
        elif tipo_unha == '9':
            return 30
        elif tipo_unha == '10':
            return 45
        else:
            raise ValueError("Tipo de unha inválido")

class Funcionario:
    def _init_(self):
        self.funcionario = []
        self.servicos = []  # Adicionando o atributo servicos

    def cadastrarFuncionario(self, nome, idade, telefone, cpf, profissao, salario):
        print(f"Funcionario: {nome}\nContato: {telefone}\nFunção: {profissao}")

        funcionario = {
            'Nome': nome,
            'Idade': idade,
            'Telefone': telefone,
            'CPF': cpf,
            'Profissao': profissao,
            'Salario': salario
        }

        print(" ")

        self.funcionario.append(funcionario)

    def adicionarServico(self, servico):
        self.servicos.append(servico)

    def listarFuncionarios(self):
        print("Funcionários Cadastrados:")
        for funcionario in self.funcionario:
            for chave, valor in funcionario.items():
                print(f'{chave}: {valor}')
            print("_______________")

    def listarServicos(self):
        print("Serviços Realizados:")
        for servico in self.servicos:
            print(servico)

    def calcularTotalServicos(self):
        total = 0
        for servico in self.servicos:
            total += servico.calcular_valor()
        return total

    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    #def get_salario(self):
        #return self.__salario
    
    #def set_salario(self, novosalario):
       # self.__salario = novosalario



trabalho = Funcionario()
trabalho.adicionarServico("hidratação")

serve = Servico()
trabalho.listarServicos()