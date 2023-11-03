class cEnfermero:
	def __init__(self, DNI, turno, estado, atendiendo_paciente):
		self.DNI = DNI
		self.turno = turno
		self.atendiendo_paciente = atendiendo_paciente
		self.estado = estado
		

def set_estado()-> None:
	
	hora_actual = time.ctime()
	print(hora_actual)


	if(cEnfermero.turno == hora_actual and cEnfermero.atendiendo_paciente == False):
		cEnfermero.estado == True
	#elif:							Ver pq tira error!!!!!!!!!!!!!!!!
		cEnfermero.estado == False
		
