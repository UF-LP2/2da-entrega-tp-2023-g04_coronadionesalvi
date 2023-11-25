import pytest

from datetime import datetime, time
from Hospital  import cHospital 
from Paciente import cPaciente 
from Medico import cMedico
from Enfermero import cEnfermero 

def test_alerta_paciente():
	paciente1 = cPaciente(1,time(8,50),"sin urgencia")
	paciente2 = cPaciente(2,time(9,50),"sin urgencia")
	paciente3 = cPaciente(3,time(20,50),"sin urgencia")
	paciente4 = cPaciente(4,time(11,50),"sin urgencia")
	paciente5 = cPaciente(5,time(12,50),"sin urgencia")
	paciente6 = cPaciente(6,time(13,50),"sin urgencia")
	lista = []
	medico = cMedico(54523523)
	medicos = [medico]
	lista.append(paciente1)
	lista.append(paciente2)
	lista.append(paciente3)
	lista.append(paciente4)
	lista.append(paciente5)
	lista.append(paciente6)
	enfermero = cEnfermero(44543673,"tarde",False,True)
	enfermeros = [enfermero]
	listaizq=[]
	listaizq.append(paciente1)
	listaizq.append(paciente2)
	listaizq.append(paciente3)
	listader=[]
	listader.append(paciente4)
	listader.append(paciente5)
	listader.append(paciente6)

	expected_alerta = "azul"

	controlar = cHospital("curitas","vicente fidel lopez 654", lista,medicos,enfermeros)

	controlar.controlar_tiempo_de_espera( listaizq, listader)

	assert lista[0].alerta == expected_alerta


	expected_estado = "azul"
	
	controlar.controlar_tiempo_de_espera( listaizq, listader)

	assert lista[1].alerta == expected_estado


	expected_estado = "azul"
	
	controlar.controlar_tiempo_de_espera( listaizq, listader)
	assert lista[2].alerta == expected_estado


	expected_estado = "azul"
	
	controlar.controlar_tiempo_de_espera( listaizq, listader)
	assert lista[3].alerta == expected_estado

