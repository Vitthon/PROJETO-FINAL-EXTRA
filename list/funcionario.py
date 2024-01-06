class Funcionario():

    def __init__(self):
        self.funcionario=[]
       

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

    def listarFuncionarios(self):
        print("Funcionários Cadastrados:")
        for funcionario in self.funcionario:
            for chave, valor in funcionario.items():
                print(f'{chave}: {valor}')
            print("_______________")

    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario

funcionarios = Funcionario()

funcionarios.cadastrarFuncionario("Vitor",20,"98202268","8283782737827","Manicure",120)
funcionarios.cadastrarFuncionario("Raiane",20,"98202268","8283782737827","Manicure",120)

funcionarios.listarFuncionarios()


