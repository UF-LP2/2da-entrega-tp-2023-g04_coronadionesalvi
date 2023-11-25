import pytest
from Hospital  import cHospital 
from Paciente import cPaciente 
from Medico import cMedico
from Enfermero import cEnfermero 

#	def __init__(self, DNI, hora_de_llegada, sintoma):

def test_ingreso_paciente():
	paciente = cPaciente(44787654, time(15,30),"sin urgencia") # creamos objeto paciente
	enfermero = cEnfermero(23767544,5,True,True)
	medico = cMedico(32576743)
	pacientes = [paciente]
	medicos = [medico]
	enfermeros = [enfermero]
	# creamos instancia
	instancia = cHospital("algo","vicente fidel lopez 894",pacientes,medicos,enfermeros)
	
	# llamamos al método ingreso_paciente
	instancia.ingreso_paciente(paciente)
	
	# verificamos que el paciente haya sido agregado correctamente
	assert paciente == instancia.pacientes[0]
