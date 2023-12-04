import pytest

from library.Hospital  import cHospital
from library.Paciente import cPaciente
from library.Medico import cMedico
from library.Enfermero import cEnfermero


def test_triagePaciente():
	#def __init__(self, DNI, turno, estado, atendiendo_paciente):
	enfermero = cEnfermero(48999098,"TARDE", True, True)
	paciente1 = cPaciente(12346345, "politraumatismo")
	pacientes = []
	enfermeros = []
	medicos = []
	hospi = cHospital("curitas", "sarmiento 1853", pacientes, medicos, enfermeros)

	# Llama al método catalogarPaciente en la instancia de cPaciente
	paciente1_mod = hospi.ingreso_paciente(paciente1)
	# Comprueba si el color del paciente se ha asignado correctamente
	assert((paciente1_mod.getNumero()== 1) == False)