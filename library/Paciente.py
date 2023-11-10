import datetime

class cPaciente:
    def __init__(self, DNI, alerta, tiempo_de_espera_maximo, estado, hora_de_llegada, sintoma, hora_ingreso_a_sala_m,numero):
        self.DNI = DNI
        self.alerta = alerta
        self.tiempo_de_espera_maximo = tiempo_de_espera_maximo
        self.estado = estado
        self.hora_de_llegada = hora_de_llegada
        self.sintoma = sintoma
        self.hora_ingreso_a_sala_m = hora_ingreso_a_sala_m
        self.numero = numero

    def getnumero(self): 
        return self.numero
    
    def set_estado(self, estado):
        self.estado = estado

    def set_hora_de_llegada(self, horaActual):
        self.hora_de_llegada = horaActual