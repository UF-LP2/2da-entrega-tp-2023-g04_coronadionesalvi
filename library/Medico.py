from library.Paciente import cPaciente              
from datetime import datetime

class cMedico:
	def __init__(self, matricula):
		self.matricula = matricula

	def medico_recibe_paciente(p: cPaciente, pacientes) -> None:
		pacientes.remove(p)	            
