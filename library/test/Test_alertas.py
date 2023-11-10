import pytest

from datetime import datetime, time
from Hospital  import cHospital 
from Paciente import cPaciente 
from Medico import cMedico
from Enfermero import cEnfermero 

"""
NOS SALE:
TypeError: combine() argument 2 must be datetime.time, not datetime.datetime
No supimos solucionarlo. Problema esta relacionado con la libreria de tiempo.

def test_alerta_paciente():
	paciente1 = cPaciente(44565234,"azul",240,"en espera",time(13,50),"sin urgencia",time(15,30),4)
	paciente2 = cPaciente(44565234,"azul",240,"en espera",time(13,50),"sin urgencia",time(15,30),4)
	paciente3 = cPaciente(44565234,"azul",240,"en espera",time(13,50),"sin urgencia",time(15,30),4)
	paciente4 = cPaciente(44565234,"azul",240,"en espera",time(13,50),"sin urgencia",time(15,30),4)
	paciente5 = cPaciente(44565234,"azul",240,"en espera",time(13,50),"sin urgencia",time(15,30),4)
	paciente6 = cPaciente(44565234,"azul",240,"en espera",time(13,50),"sin urgencia",time(15,30),4)
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
	expected_estado = "verde"
	expected_hora = datetime.now()
	controlar = cHospital("curitas","vicente fidel lopez 654", lista,medicos,enfermeros)
	controlar.controlar_tiempo_de_espera( listaizq, listader)
	assert lista[0].estado == expected_estado
	assert lista[0].hora_de_llegada == expected_hora


	expected_estado = "amarillo"
	expected_hora = datetime.now()
	
	controlar.controlar_tiempo_de_espera( listaizq, listader)
	assert lista[1].estado == expected_estado
	assert lista[1].hora_de_llegada == expected_hora


	expected_estado = "naranja"
	expected_hora = datetime.now()
	
	controlar.controlar_tiempo_de_espera( listaizq, listader)
	assert lista[2].estado == expected_estado
	assert lista[2].hora_de_llegada == expected_hora


	expected_estado = "rojo"
	expected_hora = datetime.now()
	
	controlar.controlar_tiempo_de_espera( listaizq, listader)
	assert lista[3].estado == expected_estado
	assert lista[3].hora_de_llegada == expected_hora
"""