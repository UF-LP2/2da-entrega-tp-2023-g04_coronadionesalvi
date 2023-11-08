from Paciente import cPaciente
from Enfermero import cEnfermero
from datetime import datetime

class cHospital:
	def __init__(self, nombre, direccion, cPaciente, medicos, enfermeros):
		self.nombre = nombre
		self.direccion = direccion
		self.cPaciente = cPaciente
		self.medicos = medicos
		self.enfermeros = enfermeros

	def ingreso_paciente(p: cPaciente, pacientes) -> None:
		
		enfermero = cEnfermero(cHospital.buscar_enfermero_libre())
		pacientes.append(p)

		mitad = len(pacientes)//2
		derecha = pacientes[mitad:]
		izquierda = pacientes[:mitad]
		
		if enfermero != None:
			for i in range (derecha): 
				if(p.sintoma == "politraumatismo"):
					p.alerta = "roja"
					p.triage = enfermero.DNI #atributo del paciente que guarda quien lo atendió
					enfermero.atendiendo_paciente == True
					p.hora_ingreso_a_sala_m = datetime.minute()

				elif(p.sintoma == "coma" or p.sintoma == "convulsiones" or p.sintoma == "hemorragia" or p.sintoma == "isquemia"):
					p.alerta = "naranja"
					p.triage = enfermero.DNI
					enfermero.atendiendo_paciente == True
					p.hora_ingreso_a_sala_m = datetime.minute()

				elif (p.sintoma == "cefalea" or p.sintoma == "paresia" or p.sintoma == "hipertension" or p.sintoma == "vertigo" or p.sintoma == "síncope" or p.sintoma == "urgencia_psiquiatrica"):
					p.alerta = "amarillo"
					p.triage = enfermero.DNI
					enfermero.atendiendo_paciente == True
					p.hora_ingreso_a_sala_m = datetime.minute()

				elif (p.sintoma == "otalgia" or p.sintoma == "odontalgia" or p.sintoma == "inespecifico" or  p.sintoma == "traumatismo" or p.sintoma == "esguince" ):
					p.alerta = "verde"
					p.triage = enfermero.DNI
					enfermero.atendiendo_paciente == True
					p.hora_ingreso_a_sala_m = datetime.minute()

				elif (p.sintoma == "sin_urgencia"):
					p.alerta = "azul"
					p.triage = enfermero.DNI   
					enfermero.atendiendo_paciente == True
					p.hora_ingreso_a_sala_m = datetime.minute()
				
				else:
					cHospital.medico_recibe_paciente(p)

		return cHospital.ingreso_pacientes(p, izquierda) #QUE RETORNA LA FUNCION


	def liberar_enfermero(p: cPaciente) ->  None: #seria liberar la sala  
		minutos = datetime.minute()
		segundos = datetime.second()
		enfermeros = []
		if(minutos*60 - p.hora_ingreso_a_sala_m*60 == 180):
			for i in range(len(enfermeros)):
				if(p.triage == enfermeros[i].DNI):
					cHospital(cEnfermero.set_estado())

	
	def buscar_enfermero_libre() -> cEnfermero:
		enfermeros = []
		for i in range (len(enfermeros)):
			if (enfermeros[i].estado == True):
				return enfermeros[i]
			else:
				return None

	def controlar_tiempo_de_espera() -> None:
		pacientes = []
		horaActual = datetime.now()
	
		for i in range(len(pacientes)):
			if(pacientes[i].alerta == "azul"):
				if(horaActual - pacientes[i].hora_de_llegada >= 120):
					pacientes[i].set_estado("verde")
					pacientes[i].set_hora_de_llegada(horaActual)			
				
			if(cPaciente[i].alerta == "verde"):
				if(horaActual - cPaciente[i].hora_de_llegada >= 60):
					pacientes[i].set_estado("amarillo") 
					pacientes[i].set_hora_de_llega(horaActual)

			if(pacientes[i].alerta == "amarillo"):
				if(horaActual - pacientes[i].hora_de_llegada >= 50):
					pacientes[i].set_estado("naranja")
					pacientes[i].set_hora_de_llega(horaActual)
				
			if(pacientes[i].alerta == "naranja"):
				if(horaActual - pacientes[i].hora_de_llegada >= 10):
					pacientes[i].set_estado("rojo")
					pacientes[i].set_hora_de_llega(horaActual)
				