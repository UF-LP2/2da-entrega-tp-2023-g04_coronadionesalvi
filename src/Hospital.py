from Paciente import cPaciente
from Enfermero import cEnfermero
from Medico import cMedico
from datetime import datetime

class cHospital:
	def __init__(self, nombre, direccion, pacientes, medicos, enfermeros):
		self.nombre = nombre
		self.direccion = direccion
		self.pacientes = pacientes
		self.medicos = medicos
		self.enfermeros = enfermeros

	def ingreso_paciente(self, p: cPaciente) -> None:
		
		enfermero = cEnfermero(self.buscar_enfermero_libre())
		self.pacientes.append(p)
	
		if enfermero != None:
			for i in range (len(self.pacientes)): 
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
					cMedico.medico_recibe_paciente(p)

	def liberar_enfermero(p: cPaciente) ->  None: #seria liberar la sala  
		minutos = datetime.minute()
		segundos = datetime.second()
		enfermeros = []
		if(minutos*60 - p.hora_ingreso_a_sala_m*60 == 180):
			for i in range(len(enfermeros)):
				if(p.triage == enfermeros[i].DNI):
					cHospital(cEnfermero.set_estado())

	
	def buscar_enfermero_libre(self) -> cEnfermero:
		for i in range (len(self.enfermeros)):
			if (self.enfermeros[i].estado == True):
				return self.enfermeros[i]
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
				







				




####################################################################3

#A partir de aca es lo de D&C

#
				if mitad <= 1:
#			return self.pacientes
		
		mitad = len(self.pacientes)//2
		derecha = self.pacientes[mitad:]
		izquierda = self.pacientes[:mitad]
	
		derecha = self.pacientes.mergeSort(derecha)
		izquierda = self.pacientes.mergeSort(izquierda)

		# Combina las dos mitades ordenadas en un solo array ordenado.
		return self.pacientes.merge(derecha, izquierda)
	
	
	def merge(izquierda, derecha):
		lista_resultante = []
		posicion_izq, posicion_der = 0, 0

		while posicion_izq < len(izquierda) and posicion_der < len(derecha):
			if izquierda[posicion_izq].getValor() > derecha[posicion_der].getValor() :
				lista_resultante.append(izquierda[posicion_izq])
				posicion_izq += 1
			else:
				lista_resultante.append(derecha[posicion_der])
				posicion_der += 1

		lista_resultante.extend(izquierda[posicion_izq:]) 			#extend es una funcion de libreria de python 
		lista_resultante.extend(derecha[posicion_der:])

		return lista_resultante
#