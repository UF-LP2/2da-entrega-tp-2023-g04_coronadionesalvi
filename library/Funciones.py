import csv
import string

from library.Paciente import cPaciente
from library.Medico import cMedico
from library.Enfermero import cEnfermero

def cargarPacientesCSV(archivo):
	listaPacientes = []

	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file)
		for i in fp:
			auxPac = cPaciente(i["dni"],i["espera"], i["sintoma"])

			listaPacientes.append(auxPac)

	return listaPacientes

	
def cargarMedicosCSV(archivo: string):
	listaMedicos = []
	
	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file)
		# NOCTURNO = 1
		# MANIANA = 2
		# HORAPICO = 3
		# TARDENOCHE = 4
		for i in fp:
			auxTurno = 0
			if i["turno"] == 1:
				auxTurno = 1

			elif i["turno"] == 2:
				auxTurno = 2

			elif i["turno"] == 3:
				auxTurno= 3

			else:
				auxTurno = 4

			auxBool = False
			if i["estado"] == "True":
				auxBool = True

			# dni,nombre,apellido,matricula,estado,turno
			auxMed = cMedico( i["matricula"])

			listaMedicos.append(auxMed)

	return listaMedicos