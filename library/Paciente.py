import datetime

class cPaciente:
	def __init__(self, DNI,espera, sintoma):
		self.DNI = DNI
		self.alerta = None
		#self.tiempo_de_espera_maximo = None
		# self.estado = estado
		self.espera = datetime.timedelta(minutes = 0)
		self.sintoma = sintoma
		self.hora_ingreso_a_sala_m = None
		self.numero = None

	def getnumero(self): 
		return self.numero

	def setEsperado5Min(self):
		self.espera += datetime.timedelta(minutes=5)
	
#	def set_estado(self, estado):
#		self.estado = estado

	def set_alerta(self, alerta):
		self.alerta = alerta

	def set_hora_de_llegada(self, horaActual):
		self.hora_de_llegada = horaActual