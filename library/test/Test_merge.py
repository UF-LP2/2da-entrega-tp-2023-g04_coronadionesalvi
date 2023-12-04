import pytest

from datetime import datetime, time
from library.Hospital  import cHospital 
from library.Paciente import cPaciente 
from library.Medico import cMedico
from library.Enfermero import cEnfermero 

def test_merge():
	# Prueba para una lista desordenada de pacientes
	#nombre, direccion, pacientes, medicos, enfermeros
	Paciente1= cPaciente(44727252, "politraumatismo")
	Paciente2= cPaciente (46213804, "cefalea")
	Paciente3= cPaciente(21093451, "otalgia") 

	pacientes = []
	enfermeros = []
	medicos = []
	hospi = cHospital("curitas", "sarmiento 1853", pacientes, medicos, enfermeros)

	Paciente1_mod = hospi.ingreso_paciente(Paciente1)
	Paciente2_mod = hospi.ingreso_paciente(Paciente2)
	Paciente3_mod = hospi.ingreso_paciente(Paciente3) 

	Lista_pacientes = [Paciente1_mod,Paciente2_mod,Paciente3_mod]
	lista_ordenada = cHospital.DandC(Lista_pacientes)
	
	# Verifica que la lista esté ordenada correctamente
	assert(lista_ordenada[0].DNI, 44727252)
	assert(lista_ordenada[1].DNI, 46213804)
	assert(lista_ordenada[2].DNI, 21093451)


def test2_merge():
#Prueba para una lista desordenada de otro set de pacientes

	Paciente1= cPaciente(32044451, "politraumatismo")
	Paciente2= cPaciente (21093451, "odontalgia")
	Paciente3= cPaciente(21093451, "coma") 
		
	pacientes = []
	enfermeros = []
	medicos = []
	hospi = cHospital("curitas", "sarmiento 1853", pacientes, medicos, enfermeros)

	Paciente1_mod= hospi.ingreso_paciente(Paciente1)
	Paciente2_mod= hospi.ingreso_paciente(Paciente2)
	Paciente3_mod= hospi.ingreso_paciente(Paciente3) 

	Lista_pacientes= [Paciente1_mod,Paciente2_mod,Paciente3_mod] ## le paso pacientes con colores asignados 
	
	lista_ordenada = cHospital.DandC(Lista_pacientes)
		
	# Verifica que la lista esté ordenada correctamente
	assert(lista_ordenada[0].DNI, 32044451)
	assert(lista_ordenada[1].DNI, 21093451)
	assert(lista_ordenada[2].DNI, 21093451)