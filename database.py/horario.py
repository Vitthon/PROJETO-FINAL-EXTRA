from datetime import datetime, timedelta

class SalaoDeBeleza:  #definindo classe salão de beleza
    def __init__(self, nome, horarios_disponiveis):
        self.nome = nome
        self.agenda = {}
        self.horarios_disponiveis = horarios_disponiveis

    def mostrar_horarios_disponiveis(self):  #método da classe 
        print("Horários disponíveis:")
        for horario in self.horarios_disponiveis:   
            if horario not in self.agenda or self.agenda[horario] is None:#  verifica se o horario está na agenda
                if isinstance(horario, datetime): #verifica se horário é um objeto de datetime, verifica se horario é um objeto do tipo datetime
                    print(horario.strftime("%Y-%m-%d %H:%M")) 
                else:
                    print(horario)  
                    

if __name__ == "__main__":  
        horarios_disponiveis = [ 
            datetime(2024, 3, 1, 10, 0),  
            datetime(2024, 4, 1, 11, 0),
            datetime(2024, 5, 2, 14, 0),
            datetime(2024, 6, 19, 15, 0),
            datetime(2024, 9, 6, 8, 0 )]
        salao = SalaoDeBeleza("Salão Cabeleleila Leila", horarios_disponiveis)  
        salao.mostrar_horarios_disponiveis() 
        
