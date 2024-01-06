from agendamento import Agendamento
from funcionario import Funcionario
from financas import Financas

class Gerente(Funcionario):
    def __init__(self):
        pass

    def cadastrar_funcionario(self, nome, idade, telefone, email, cpf, profissao, salario):
        print(f"Funcionário: {nome}\nContato: {telefone} Email: {email}\nFunção: {profissao}")

    def agendar_horario(self, agendamento):
        data_agendamento = agendamento.marcar_data
        pagamento = agendamento.forma_pagamento
        servico = agendamento.tipo_servico

    def pagar_funcionarios(self, funcionarios):
        for funcionario in funcionarios:
            profissao = funcionario.profissao
            if profissao == 'Cabeleireiro':
                funcionario.set_salario(5000)
            elif profissao == 'Manicure':
                funcionario.set_salario(3000)

    def desconto_de_saldo(self, saldo, salario):
        return saldo - salario


gerente = Gerente()

# Criando instâncias de Funcionario
funcionario1 = Funcionario("Vitor",20,"98202268", "texto","8283782737827","Manicure",120)
funcionario2 = Funcionario("Vr",20,"98202268", "texto","8283782737827","Manicure",120)

gerente.cadastrar_funcionario(funcionario1.nome, funcionario1.idade, funcionario1.telefone, funcionario1.email, funcionario1.cpf, funcionario1.profissao, funcionario1.salario)
gerente.cadastrar_funcionario(funcionario2.nome, funcionario2.idade, funcionario2.telefone, funcionario2.email, funcionario2.cpf, funcionario2.profissao, funcionario2.salario)

# Agendar um horário
agendamento1 = Agendamento("2023-01-01", "Débito", "Corte")
gerente.agendar_horario(agendamento1)

# Pagar os funcionários
funcionarios = [funcionario1, funcionario2]
gerente.pagar_funcionarios(funcionarios)

# Exibir o saldo após o desconto
saldo_atualizado = gerente.desconto_de_saldo(Financas.saldo, funcionario1.salario)
print(f"Saldo após desconto: {saldo_atualizado}")

    




