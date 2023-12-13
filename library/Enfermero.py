from datetime import datetime

class cEnfermero:
	def __init__(self, DNI, turno, estado, atendiendo_paciente):
		self.DNI = DNI
		self.turno = turno
		self.atendiendo_paciente = atendiendo_paciente
		self.estado = estado
		

	def set_estado(self)-> None:
	
		hora_actual = datetime.now()

		if(self.turno == hora_actual and self.atendiendo_paciente == False):
			self.estado == True
		else:
			self.estado == False

		print(self.estado)
		
