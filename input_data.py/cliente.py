import re
class Cliente:
    
    def _init_(self, nome, cpf, telefone):
        self.nome = nome
        self._cpf = self.validarcpf(cpf)    #privando meu cpf e telefone(encapsulando)
        self._telefone = self.validartelefone(telefone) #Chama o método validartelefone da instância atual da classe Cliente, passando o número de telefone (telefone) como argumento. 
               
    def informacoesCliente(self):  
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
    
    
    def get_nome(self):   #metodo para obter os valores dos atributos privados da minha classe cliente
        return self.nome  
    
    def get_cpf(self):
        return self._cpf
    
    def get_telefone(self):
        return self._telefone  
    
    
from abc import ABC, abstractmethod

class Servico(ABC): #A composição ocorre quando uma classe é composta por objetos de outras classes. 
    @abstractmethod
    def _init_(self, cliente):  #construtor que recebe um objeto
        self.cliente = cliente
    def calcular_valor(self):
        raise NotImplementedError("Método calcular_valor deve ser implementado nas classes filhas.") #serve de base para outras classes, pq tem o metodo q as outras vão precisar
        # execessão informando q o metodo deve ser implementado em outra classe
    
class ServicoCabelo(Servico):
    def _init_(self, cliente, tamanho_cabelo):   #herda da classe abstrata Servico. Seu construtor  recebe um objeto cliente
        self.taxa = self._calcular_taxa(tamanho_cabelo) #recebe o metodo calcular taxa e tamanho do cabelo
        super()._init_(cliente)
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
            return self.taxa * 100 + 100 #retornar a taxa mais o valor fixo
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
    def _init_(self, cliente):
        super()._init_( cliente)
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




#entrada de usuario e criando uma instancia 
nome = input("Digite seu nome: ")   
cpf = input("Digite seu CPF: ")
telefone = input("Digite o número do seu telefone: ")

cliente = Cliente(nome,cpf,telefone)   #criando um objeto da classe Cliente
cliente.informacoesCliente()  #chamando meu método para imprimir as informações 

opcao_cabelo = input("----- CABELO: -----\n 1. Mecha\n 2. Corte\n 3. Tintura\n 4. Hidratação\n 5. Progressiva\n 6. Escova\n") #atributo para opção
tamanho_cabelo = input("Informe o comprimento do cabelo (curto, medio, longo):\n ") #informar tamanho do cabelo

servico_cabelo = ServicoCabelo(cliente, tamanho_cabelo)  #criando um objeto
valor_cabelo = servico_cabelo.calcular_valor(opcao_cabelo) #chamando o obj mais o metodo calcular o valor
print("Valor do serviço de cabelo:", valor_cabelo, "\n")

tipo_unha = input("----- UNHAS: -----\n 7. Alongamento em fibra\n 8. Esmaltação em Gel\n 9. Unhas Simples\n 10. Unhas Postiças\n")
servico_unha = ServicoUnha(cliente) 
valor_unha = servico_unha.calcular_valor(tipo_unha)
print("Valor do serviço de unha:",valor_unha)