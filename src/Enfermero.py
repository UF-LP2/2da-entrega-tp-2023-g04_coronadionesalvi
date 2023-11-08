from datetime import datetime

class cEnfermero:
	def __init__(self, DNI, turno, estado, atendiendo_paciente):
		self.DNI = DNI
		self.turno = turno
		self.atendiendo_paciente = atendiendo_paciente
		self.estado = estado
		

def set_estado()-> None:
	
	hora_actual = datetime.now()
	
	if(cEnfermero.turno == hora_actual and cEnfermero.atendiendo_paciente == False):
		cEnfermero.estado == True
	else:
		cEnfermero.estado == False
		
