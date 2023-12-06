import csv
import string

from library.Paciente import cPaciente
from library.Medico import cMedico
from library.Enfermero import cEnfermero

def cargarPacientesCSV(archivo: string):
	listaPacientes = []

	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file) #dictreader es para recorrer el archivo en columnas 
		for i in fp:
			auxPac = cPaciente(i["DNI"], i["sintoma"])

			listaPacientes.append(auxPac)

	return listaPacientes

	
def cargarMedicosCSV(archivo: string):
	listaMedicos = []
	
	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file)
		
		for i in fp:
		
			auxMed = cMedico( i["matricula"])
			listaMedicos.append(auxMed)

	return listaMedicos