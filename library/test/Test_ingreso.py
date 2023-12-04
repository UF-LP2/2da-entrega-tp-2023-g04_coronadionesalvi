import pytest
from library.Hospital  import cHospital 
from library.Paciente import cPaciente 
from library.Medico import cMedico
from library.Enfermero import cEnfermero 

def test_ingreso_paciente():
    
	paciente = cPaciente(44787654, "sin urgencia") # creamos objeto paciente
	enfermero = cEnfermero(23767544,5,True,True)
	medico = cMedico(32576743)
	pacientes = [paciente]
	medicos = [medico]
	enfermeros = [enfermero]
	# creamos instancia
	instancia = cHospital("curitas","vicente fidel lopez 894",pacientes,medicos,enfermeros)
	
	# llamamos al método ingreso_paciente
	instancia.ingreso_paciente(paciente)
	
	# verificamos que el paciente haya sido agregado correctamente
	assert paciente == instancia.pacientes[0]
