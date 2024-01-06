import re
class Cliente:
    
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self._cpf = self.validarcpf(cpf)    #privando cpf e telefone(encapsulando)
        self._telefone = self.validartelefone(telefone)
               
    def informacoesCliente(self):   #usando regex para validar cpf e telefone
        print(f'Cliente: {self.nome}\nCPF: {self._cpf}\n Telefone: {self._telefone}')


    def validarcpf(self, cpf):
        padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}[\-]*\d{2}')
        if padrao_cpf.match(cpf):
            return cpf
        else:
            raise ValueError("O CPF está inválido")
        
    def validartelefone(self, telefone):
        padrao_telefone = re.compile(r'^[\(]\d{2}[)]\s\d{4,5}[\-]\d{4}$') 
        if padrao_telefone.match(telefone):#para verificar se o cpf está dentro dos padrões
            return telefone
        else:
            raise ValueError("O telefone está inválido")  #exceção caso o telefone não cumpra com os padrões
    
    
    def get_nome(self):   #metodo para obter os valores dos atributos privados da classe cliente
        return self.nome  
    
    def get_cpf(self):
        return self._cpf
    
    def get_telefone(self):
        return self._telefone  
            
         

#entrada de usuario e criando uma instancia 
nome = input("Digite seu nome completo: ")   
cpf = input("Digite seu CPF: ")
telefone = input("Digite o número do seu telefone: ")

cliente = Cliente(nome,cpf,telefone)   #criando um objeto da classe Cliente
cliente.informacoesCliente()  #chamando o  método para imprimir as informações dos clientes