from library.Paciente import cPaciente
from library.Enfermero import cEnfermero
from library.Medico import cMedico
from datetime import datetime, time

class cHospital:
	def __init__(self, nombre, direccion, pacientes, medicos, enfermeros):
		self.nombre = nombre
		self.direccion = direccion
		self.pacientes = pacientes
		self.medicos = medicos
		self.enfermeros = enfermeros


	def ingreso_paciente(self, p) -> None:
		
		enfermero = self.buscar_enfermero_libre()
	
		if enfermero != None:
			if(p.sintoma == "politraumatismo"):
				p.alerta = "roja"
				p.setNumero(0)

			elif(p.sintoma == "coma" or p.sintoma == "convulsiones" or p.sintoma == "hemorragia" or p.sintoma == "isquemia"):
				p.alerta = "naranja"
				p.setNumero(1)
				enfermero.atendiendo_paciente == True

			elif (p.sintoma == "cefalea" or p.sintoma == "paresia" or p.sintoma == "hipertension" or p.sintoma == "vertigo" or p.sintoma == "síncope" or p.sintoma == "urgencia_psiquiatrica"):
				p.alerta = "amarillo"
				p.setNumero(2)
				enfermero.atendiendo_paciente == True

			elif (p.sintoma == "otalgia" or p.sintoma == "odontalgia" or p.sintoma == "inespecifico" or  p.sintoma == "traumatismo" or p.sintoma == "esguince" ):
				p.alerta = "verde"
				p.setNumero(3)
				enfermero.atendiendo_paciente == True

			elif (p.sintoma == "sin_urgencia"):
				p.alerta = "azul"
				p.setNumero(4)
				enfermero.atendiendo_paciente == True
			
			else:
				cMedico.medico_recibe_paciente(p,self.pacientes)
		self.pacientes.append(p)
		return p


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
		return cHospital.merge(izquierda, derecha)
	
	def merge(izquierda, derecha):#Recibe las dos mitades ordenadas (izquierda y derecha) como parámetros. 
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

	def adelantar10Min(self):				#Cuando se llama se actualizan los tiempos de espera de los pacientes 
		for i in self.pacientes():
			i.setEsperado10Min()

#cada vez que invoco esta funcion se chequean los tiempos de todos los pacientes
#y cada vez que se termine de ejecutar el for avanza 10min el programa
	def controlar_tiempo_de_espera(self, izquierda, derecha) -> None: 
		self.pacientes = self.merge(izquierda,derecha)
		for i in range (len(self.pacientes)):
			
			if(self.pacientes[i].alerta == "azul"):
				if(self.pacientes[i].getEspera() >= datetime.timedelta(minutes=120)):
					self.pacientes[i].set_alerta("verde")			
			if(self.pacientes[i].alerta == "verde"):
				if(self.pacientes[i].getEspera() >= datetime.timedelta(minutes=60)):
					self.pacientes[i].set_alerta("amarillo") 
			if(self.pacientes[i].alerta == "amarillo"):
				if(self.pacientes[i].getEspera() >= datetime.timedelta(minutes=50)):
					self.pacientes[i].set_alerta("naranja")
			if(self.pacientes[i].alerta == "naranja"):
				if(self.pacientes[i].getEspera() >= datetime.timedelta(minutes=10)):
					self.pacientes[i].set_alerta("rojo")
		self.adelantar10Min()

	def getPacientesString(self):
		lista = []
		aux = ""
		for i in self.pacientes:
			aux = i.DNI + " " + i.sintoma + " " + str(i.espera)
			lista.append(aux)
		return lista

	def getMedicosString(self):
		lista = []
		aux = ""
		for i in self.medicos:
			aux = i.matricula + " " 
			lista.append(aux)
		return lista

	def imprimir(self):
				for i in self.pacientes:
					print(i.dni, i.espera, i.sintoma)
					print("\n")