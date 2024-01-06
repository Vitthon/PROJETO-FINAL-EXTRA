from datetime import datetime
from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def registrar_pagamento(self, cliente, valor, forma, servico, dataPagamento = None):
        pass

class Financas(Pagamento):

    def __init__(self, saldo):
        self.__saldo = saldo
        self.historico_pagamentos = []


    '''Métodos Getters e Setters do saldo'''
    @property
    def saldoDoSalao(self):
        return self.__saldo
    
    @saldoDoSalao.setter
    def saldoDoSalao(self, atualiza_saldo):
        self.__saldo =+ atualiza_saldo
        return atualiza_saldo
        

    '''Método para registrar os pagementos '''
    def registrar_pagamento(self, cliente, valor, forma, servico, dataPagamento = None):
        '''Se o dataPagamento for vazio (None) recebe a função datetime'''
        if dataPagamento == None:
            dataPagamento = datetime.now().date()

        '''Dicionario que registra os pagamentos'''
        pagamentos = {'Cliente': cliente, 'Valor': valor, 'Forma de pagamento': forma, 'Serviço': servico, 'Pagamento Realizado em': dataPagamento}
        print(" ")

        '''Acrescenta os pagamentos realizados a uma lista para depois imprimir todos de uma vez'''
        self.historico_pagamentos.append(pagamentos)

        '''Exibe os pagamentos'''
        for chave, valor in pagamentos.items():
            print(f'{chave}: {valor}')


          
        '''Se a chave for igual 'Valor', acrescenta ao valor da variavel saldo'''
        if chave == 'Valor':
                self.__saldo += valor
   
        '''Exibe o historico de pagamentos e exibe o saldo final'''
    def mostar_historico_pagamentos(self):
        print(" ")
        print("Histórico de Pagamentos:\n")
        for pagamento in self.historico_pagamentos:
            for chave, valor in pagamento.items():
                print(f'{chave}: {valor}')
            print("________________")

        print(f'Saldo Final: {self.__saldo}')
   


financiamento = Financas(100)

financiamento.registrar_pagamento("Vitor", 50, "Pix", "Luzes")
financiamento.registrar_pagamento("Raiane", 30, "Cartão", "Abrir Cachos")

financiamento.mostar_historico_pagamentos()


