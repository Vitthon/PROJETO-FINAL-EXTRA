from datetime import datetime, timedelta
class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Agendamento:
    def __init__(self, cliente, horario):
        self.cliente = cliente()
        self.horario = horario()
        
        
class MixinSalao: 
    
    def __init__(self, config):
        self.config = config
        self.agenda = {}  # atributo agenda como dicionario
        self.horarios_disponiveis = []
    '''classe mixinsalao para agregar funcionalidades de horarios '''
    def mostrar_horarios_disponiveis(self):
        print("Horários disponíveis:")
        for horario in self.horarios_disponiveis:
            if horario not in self.agenda or self.agenda[horario] is None:
                if isinstance(horario, datetime):
                    print(horario.strftime("%Y-%m-%d %H:%M"))
                else:
                    print(horario)
        

    def adicionar_horario_disponivel(self, horario):
        self.horarios_disponiveis.append(horario)  
            # método append adiciona um elemento no final da lista
            
    def remover_horario_disponivel(self, horario):
        if horario in self.horarios_disponiveis:  #verifica se o horario está presente na lista
            self.horarios_disponiveis.remove(horario)  
            print(f"Horário removido: {horario.strftime('%Y-%m-%d %H:%M')}")
        else:
            print(f"Horário {horario.strftime('%Y-%m-%d %H:%M')} não encontrado na lista de disponíveis.")
            # o método é usado  para remover um horario da lista


    def agendar_horario(self, cliente, horario):
        if horario in self.horarios_disponiveis: # para verificr se o horairo informado está na lista
            if self.agenda.get(horario) is None: 
                self.agenda[horario] = Agendamento(cliente, horario)  # verifica se o horario não está agendado
                print(f"Agendamento realizado para {cliente.nome} às" 
                      f"{horario.strftime('%Y-%m-%d %H:%M')}")
                self.remover_horario_disponivel(horario)  
            else:
                print(f"Horário {horario.strftime('%Y-%m-%d %H:%M')} já está ocupado.")  
        else:
            print(f"Horário {horario.strftime('%Y-%m-%d %H:%M')} não está disponível.")  
            

    def alterar_horario(self, horario_antigo, horario_novo):
        if horario_antigo in self.agenda and self.agenda[horario_antigo] is not None: #verifica se o horario antigo está na agenda
            agendamento = self.agenda.pop(horario_antigo)  # remove o horario antigo
            self.agenda[horario_novo] = agendamento # adiciona o novo horario na agenda
            self.adicionar_horario_disponivel(horario_antigo) 
            print(f"Horário alterado para {  horario_novo.strftime('%Y-%m-%d %H:%M')}")  
            # para informar que o horario foi alterado
        else:
            print(f"Horário {horario_antigo.strftime('%Y-%m-%d %H:%M')} não encontrado ou está vago.")
            
class SalaoDeBeleza(MixinSalao):  #utilizando o mixinsalao por meio de herança
    def __init__(self, nome, horarios_disponiveis):
        self.nome = nome
        self.agenda = {}
        self.horarios_disponiveis = horarios_disponiveis


if __name__ == "__main__":
    cliente1 = Cliente("Demetria")
    cliente2 = Cliente("Raquel")
    cliente3 = Cliente("Vitória")
    cliente4 = Cliente("Raiane")
    cliente5 = Cliente("Júlia")
    horarios_disponiveis = [
            datetime(2024, 3, 1, 10, 0),
            datetime(2024, 4, 1, 11, 0),
            datetime(2024, 5, 2, 14, 0),
            datetime(2024, 6, 19, 15, 0),
            datetime(2024, 9, 6, 8, 0 ),
            datetime(2024, 9, 16, 17, 0),
            datetime(2024, 11, 12, 18, 0),
            datetime(2024, 5, 2, 14, 0)]
    
    salao = SalaoDeBeleza("Salão Cabeleleila Leila", horarios_disponiveis)
    salao.mostrar_horarios_disponiveis()  #horarios disponiveis do mixin foi chamado em uma instancia de salao
    horario1 = datetime(2024, 3, 1, 10, 0)
    salao.agendar_horario(cliente1,horario1)
    salao.mostrar_horarios_disponiveis()
    novo_horario = datetime(2024, 4, 1, 11, 0)
    salao.alterar_horario(horario1, novo_horario)
    salao.mostrar_horarios_disponiveis()
    horario2 = datetime(2024, 6, 19, 15, 0)
    salao.agendar_horario(cliente2, horario2)
    salao.mostrar_horarios_disponiveis()
    horario5 = datetime(2024, 11, 12, 18, 0)    
    salao.agendar_horario(cliente3, horario5)
    salao.mostrar_horarios_disponiveis()

