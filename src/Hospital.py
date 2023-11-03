from Paciente import cPaciente
from Enfermero import cEnfermero

class cHospital:
	def __init__(self, nombre, direccion, cPaciente, medicos, enfermeros):
		self.nombre = nombre
		self.direccion = direccion
		self.cPaciente = cPaciente
		self.medicos = medicos
		self.enfermeros = enfermeros

	def ingreso_paciente(p: cPaciente) -> None:
		
		enfermero = cEnfermero(buscar_enfermero_libre())
		cPaciente.append(p)
		#pacientes = []
		
		if enfermero != nullptr:

			if(p.sintoma == "politraumatismo"):
				p.alerta = "roja"
				p.triage = enfermero.DNI #atributo del paciente que guarda quien lo atendió
				enfermero.atendiendo_paciente == True

			elif(p.sintoma == "coma" or p.sintoma == "convulsiones" or p.sintoma == "hemorragia" or p.sintoma == "isquemia"):
				p.alerta = "naranja"
				p.triage = enfermero.DNI
				enfermero.atendiendo_paciente == True

			elif (p.sintoma == "cefalea" or p.sintoma == "paresia" or p.sintoma == "hipertension" or p.sintoma == "vertigo" or p.sintoma == "síncope" or p.sintoma == "urgencia_psiquiatrica"):
				p.alerta = "amarillo"
				p.triage = enfermero.DNI
				enfermero.atendiendo_paciente == True

			elif (p.sintoma == "otalgia" or p.sintoma == "odontalgia" or p.sintoma == "inespecifico" or  p.sintoma == "traumatismo" or p.sintoma == "esguince" ):
				p.alerta = "verde"
				p.triage = enfermero.DNI
				enfermero.atendiendo_paciente == True

			elif (p.sintoma == "sin_urgencia"):
				p.alerta = "azul"
				p.triage = enfermero.DNI   
				enfermero.atendiendo_paciente == True

			else:
				medico_recibe_paciente(p)

	def liberar_sala(p: cPaciente) ->  None:
		hora_actual = datetime.datetime.now().time()
		minutos = hora_actual.minute
		if(minutos == 0):

		#else:
			minutos_actual = minutos * 60
		enfermeros = []
		pacientes = []

		if(enfermeros.atendiendo_paciente == True):
			if(hora_ingreso_pac - minutos_actual == 180 ): #hora_ingreso_pac es la hora en la que el pac entra a la sala del enfermero 
				enfermeros.atendiendo_paciente = False 	#hora_ingreso_pac y hora_actual quiero agarrar solo los minutos y pasarlos a segundos
				pacientes.remove(p)						

	def buscar_enfermero_libre() -> cEnfermero:
		enfermeros = []
		for i in range (len(enfermeros)):
			if (enfermeros[i].estado == True):
				return enfermeros[i]
			else:
				return None

	def controlar_tiempo_de_espera() -> None:
		pacientes = []
		hora.actual = time.ctime()
	
		for i in range(len(pacientes)):
			if(pacientes[i].alerta == "azul"):
				if(hora.actual - pacientes[i].hora_de_llegada >= 120):
					pacientes[i].set_estado("verde")
					pacientes[i].set_hora_de_llegada(hora.actual)			
				
			if(cPaciente[i].alerta == "verde"):
				if(hora.actual - cPaciente[i].hora_de_llegada >= 60):
					pacientes[i].set_estado("amarillo") 
					pacientes[i].set_hora_de_llega(hora.actual)

			if(pacientes[i].alerta == "amarillo"):
				if(hora.actual - pacientes[i].hora_de_llegada >= 50):
					pacientes[i].set_estado("naranja")
					pacientes[i].set_hora_de_llega(hora.actual)
				
			if(pacientes[i].alerta == "naranja"):
				if(hora.actual - pacientes[i].hora_de_llegada >= 10):
					pacientes[i].set_estado("rojo")
					pacientes[i].set_hora_de_llega(hora.actual)
				