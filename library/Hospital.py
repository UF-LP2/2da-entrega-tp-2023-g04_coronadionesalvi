from Paciente import cPaciente
from Enfermero import cEnfermero
from Medico import cMedico
from datetime import datetime, time

class cHospital:
	def __init__(self, nombre, direccion, pacientes, medicos, enfermeros):
		self.nombre = nombre
		self.direccion = direccion
		self.pacientes = pacientes
		self.medicos = medicos
		self.enfermeros = enfermeros


	def ingreso_paciente(self, p: cPaciente) -> None:
		
		enfermero = self.buscar_enfermero_libre()
		self.pacientes.append(p)
	
		if enfermero != None:
			if(p.sintoma == "politraumatismo"):
				p.alerta = "roja"
				p.numero = 0
				p.triage = enfermero.DNI #atributo del paciente que guarda quien lo atendió					enfermero.atendiendo_paciente == True					p.hora_ingreso_a_sala_m = datetime.minute()

			elif(p.sintoma == "coma" or p.sintoma == "convulsiones" or p.sintoma == "hemorragia" or p.sintoma == "isquemia"):
				p.alerta = "naranja"
				p.numero = 1
				p.triage = enfermero.DNI
				enfermero.atendiendo_paciente == True
				p.hora_ingreso_a_sala_m = datetime.minute()

			elif (p.sintoma == "cefalea" or p.sintoma == "paresia" or p.sintoma == "hipertension" or p.sintoma == "vertigo" or p.sintoma == "síncope" or p.sintoma == "urgencia_psiquiatrica"):
				p.alerta = "amarillo"
				p.numero = 2
				p.triage = enfermero.DNI
				enfermero.atendiendo_paciente == True
				p.hora_ingreso_a_sala_m = datetime.minute()

			elif (p.sintoma == "otalgia" or p.sintoma == "odontalgia" or p.sintoma == "inespecifico" or  p.sintoma == "traumatismo" or p.sintoma == "esguince" ):
				p.alerta = "verde"
				p.numero = 3
				p.triage = enfermero.DNI
				enfermero.atendiendo_paciente == True
				p.hora_ingreso_a_sala_m = datetime.minute()

			elif (p.sintoma == "sin_urgencia"):
				p.alerta = "azul"
				p.numero = 4
				p.triage = enfermero.DNI   
				enfermero.atendiendo_paciente == True
				p.hora_ingreso_a_sala_m = datetime.minute()
			
			else:
				cMedico.medico_recibe_paciente(p,self.pacientes)

	def liberar_enfermero(p: cPaciente) ->  None: #seria liberar la sala  
		minutos = datetime.minute()
		segundos = datetime.second()
		enfermeros = []
		if(minutos*60 - p.hora_ingreso_a_sala_m*60 == 180):
			for i in range(len(enfermeros)):
				if(p.triage == enfermeros[i].DNI):
					enfermeros[i].set_estado()

	
	def DandC(pacientes): 
		mitad = len(pacientes)//2
		if mitad <= 1: 					#(DandC) metodo divide and conquer. ordenar una lista de pacientes. recibe la lista de pacientes como parámetro.
			return pacientes
		
		derecha = pacientes[mitad:]
		izquierda = pacientes[:mitad]				#ORDENA 
	
		derecha = pacientes.DandC(derecha)
		izquierda = pacientes.DandC(izquierda)

		# Combina las dos mitades ordenadas en un solo array ordenado.
		return pacientes.merge(izquierda, derecha)
	
	def merge(self,izquierda, derecha):#Recibe las dos mitades ordenadas (izquierda y derecha) como parámetros. 
		lista_resultante = []		#La función crea una lista vacía llamada "lista_resultante" para almacenar los elementos ordenados.
		
		posicion_izq = 0		
		posicion_der = 0		#indican la posición actual en cada mitad.
		

		while posicion_izq < len(izquierda) and posicion_der < len(derecha) and posicion_izq < posicion_der: 
			if (izquierda[posicion_izq].getnumero() > derecha[posicion_der].getnumero()): #ordena por nro de color 0 rojo 4 azul
				lista_resultante.append(izquierda[posicion_izq])
				posicion_izq += 1
			else:
				lista_resultante.append(derecha[posicion_der])
				posicion_der += 1

		lista_resultante.extend(izquierda[posicion_izq:]) 			#"extend" para agregar los elementos restantes de la mitad izquierda y de la mitad derecha a la lista resultante. 
		lista_resultante.extend(derecha[posicion_der:])

		return lista_resultante

	def buscar_enfermero_libre(self) -> cEnfermero:
		for i in range (len(self.enfermeros)):
			if (self.enfermeros[i].estado == True):
				return self.enfermeros[i]
			else:
				return None

	def controlar_tiempo_de_espera(self, izquierda, derecha) -> None:
		horaActual = datetime.now().time()
		lista = self.merge(izquierda,derecha)

		horaActual = datetime.combine(datetime.today(), horaActual)

		for i in range (len(lista)):
			hora = lista[i].hora_de_llegada.hour
			minuto = lista[i].hora_de_llegada.minute
			# segundo = lista[i].hora_de_llegada.second

			aux_lista = datetime.time(hora,minuto)
			lista[i].hora_de_llegada = datetime.combine(horaActual, aux_lista)
			aux = horaActual - lista[i].hora_de_llegada
			
			totalMin = aux.total_seconds() / 60
			if(lista[i].alerta == "azul"):
				if(totalMin >= 120):
					lista[i].set_alerta("verde")
					lista[i].set_hora_de_llegada(horaActual)			
				
			if(lista[i].alerta == "verde"):
				if(totalMin >= 60):
					lista[i].set_alerta("amarillo") 
					lista[i].set_hora_de_llegada(horaActual)

			if(lista[i].alerta == "amarillo"):
				if(totalMin >= 50):
					lista[i].set_alerta("naranja")
					lista[i].set_hora_de_llegada(horaActual)
				
			if(lista[i].alerta == "naranja"):
				if(totalMin >= 10):
					lista[i].set_alerta("rojo")
					lista[i].set_hora_de_llegada(horaActual)

	def suma_numeros(a,b) : #metodo de prueba
		suma = a + b
		return suma
	