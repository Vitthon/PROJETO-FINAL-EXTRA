'''

import pandas 
import csv
class Produto:
    def __init__(self):
        pass

    
    Mostra lista com colunhas divididas, quantidade de linhas e no final faz soma da coluna produto 
    através da biblioteca panda 
    
    def mostra_produtos(self):
        tabela = pandas.read_csv("list/listaprodutos.csv")
        print(tabela)
        print(f"Total investido em Produtos:")
        print((tabela["VALOR"].sum()))


        
Produto.mostra_produtos("list/listaprodutos.csv")
'''

import pandas as pd

class Produto:
    def __init__(self):
        pass


    
    def adiciona_produto(self):
        # Solicitar os dados ao usuário
        nome_produto = str (input("Digite o nome do produto: "))
        quantidade = str(input("Digite a quantidade: "))
        valor = int(input("Digite o valor: "))
        caminho_arquivo = 'list/listaprodutos.csv'
        # Criar um dicionário com os dados do novo produto
        novo_produto = {
            'PRODUTO': nome_produto,
            'DESCRICAO': quantidade,
            'VALOR': valor
        }

        # Ler o arquivo CSV existente

        try:
            tabela = pd.read_csv(caminho_arquivo)
        except FileNotFoundError:
            # Se o arquivo não existir, criar um DataFrame vazio
            tabela = pd.DataFrame(columns=['PRODUTO', 'DESCRICAO', 'VALOR'])

        if tabela.empty:
            tabela = pd.DataFrame(columns=['PRODUTO', 'DESCRICAO', 'VALOR'])
            return tabela.append (novo_produto, ignore_index=True)
        # Adicionar a nova linha ao DataFrame
        # Salvar o DataFrame de volta no arquivo CSV
        tabela.to_csv("list/listaprodutos.csv", index=False, header=True)


        print("Produto adicionado com sucesso!")

    def mostra_produtos(self):
        try:
            tabela = pd.read_csv("list/listaprodutos.csv")
            print(tabela)
            print(f"Total investido em Produtos:")
            print((tabela["VALOR"].sum()))
        except FileNotFoundError:
            print("O arquivo CSV ainda não existe.")

# Criar uma instância da classe Produto
produto = Produto()

# Adicionar um novo produto


# Mostrar a tabela de produtos
produto.mostra_produtos()

produto.adiciona_produto()
produto.mostra_produtos()


'''
import pandas as pd


class Produto:
    def __init__(self):
        pass

    def adiciona_produto(self):
               # Solicitar os dados ao usuário
        nome_produto = str (input("Digite o nome do produto: "))
        quantidade = str(input("Digite a quantidade: "))
        valor = int(input("Digite o valor: "))

        # Criar um dicionário com os dados do novo produto
        novo_produto = {
            'PRODUTO': nome_produto,
            'DESCRICAO': quantidade,
            'VALOR': valor
        }

        # Ler o arquivo CSV existente
        try:
            tabela = pd.read_csv("list/listaprodutos.csv")
        except FileNotFoundError:
            # Se o arquivo não existir, criar um DataFrame vazio
            tabela = pd.DataFrame(columns=['PRODUTO', 'DESCRICAO', 'VALOR'])

        # Adicionar a nova linha ao DataFrame
        tabela = tabela.append(novo_produto, ignore_index=True)

        # Salvar o DataFrame de volta no arquivo CSV sem incluir o índice
        tabela.to_csv("list/listaprodutos.csv", index=False, header=True)

        print("Produto adicionado com sucesso!")

    def mostra_produtos(self):
        try:
            tabela = pd.read_csv("list/listaprodutos.csv")
            print(tabela)
            print(f"Total investido em Produtos:")
            print((tabela["VALOR"].sum()))
        except FileNotFoundError:
            print("O arquivo CSV ainda não existe.")

# Criar uma instância da classe Produto
produto = Produto()

# Adicionar um novo produto
produto.adiciona_produto()

# Mostrar a tabela de produtos
produto.mostra_produtos()
'''




