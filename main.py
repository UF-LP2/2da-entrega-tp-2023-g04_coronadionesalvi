import csv

from datetime import datetime, time
from library.Enfermero import cEnfermero
from library.Hospital import cHospital
from library.Medico import cMedico
from library.Paciente import cPaciente


def cargarPacientesCSV(archivo): #nombre del archivo como string
	listaPacientes = []			#lista vacia de pacientes

	with open(archivo, mode="r") as file:			#mode read --> archivo leido
		fp = csv.DictReader(file)					#leo el archivo por columna
		for i in fp:

			auxPac = cPaciente(i["dni"], i["hora_llegada"],i["sintoma"])	# i mueve por fila, y se lee por columna 

			listaPacientes.append(auxPac)

	return listaPacientes


def main() -> None:
    pacientes = cargarPacientesCSV("Pacientes.csv")
    print("Hello World")


if __name__ == "__main__":
	main()


