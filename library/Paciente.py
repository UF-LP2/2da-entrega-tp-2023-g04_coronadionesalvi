import datetime

class cPaciente:
	def __init__(self, DNI, sintoma):
		self.DNI = DNI
		self.alerta = None
		self.espera = datetime.timedelta(minutes = 0)		# arranca en 0
		self.sintoma = sintoma
		self.hora_ingreso_a_sala_m = None
		self.numero = None

	def getNumero(self): 
		return self.numero

	def setNumero(self, n): 
		self.numero = n

	def getEspera(self): 
		return self.espera

	def setEsperado10Min(self):
		self.espera += datetime.timedelta(minutes=10)

	def set_alerta(self, alerta):
		self.alerta = alerta

