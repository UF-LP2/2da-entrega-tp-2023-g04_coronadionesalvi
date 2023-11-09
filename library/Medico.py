from Paciente import cPaciente              
from datetime import datetime

class cMedico:
	def __init__(self, matricula):
		self.matricula = matricula

	def medico_recibe_paciente(p: cPaciente) -> None:
		pacientes = []
		pacientes.remove(p)	            
