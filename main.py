from library.Enfermero import cEnfermero
from library.Hospital import cHospital
from library.Medico import cMedico
from library.Paciente import cPaciente



def main() -> None:
	pacientes = [paciente,paciente2,paciente3,paciente4]
	enfermeros = [enfermero,enfermero2,enfermero3,enfermero4]
	medicos = [medico,medico1,medico2,medico3]
	
	hospital = cHospital("Curitas","Vicente Fidel Lopez 543, caballito",pacientes,medicos,enfermeros)

	enfermero = cEnfermero(43567555,"noche",False,False)
	enfermero2 = cEnfermero(23765654,"tarde",False,False)
	enfermero3 = cEnfermero(23223456,"maniana",True, False)
	enfermero4 = cEnfermero(34574654,"noche",False, True)
	
	medico = cMedico(3254365)
	medico1 = cMedico(4325211)
	medico2 = cMedico(123513)
	medico3 = cMedico(324652)

	paciente = cPaciente(44787654,"azul",240,"en espera","08:30","sin urgencia","09:30",4)
	paciente2 = cPaciente(22787654,"verde",120,"en espera","15:00","esguince","16:30",3)
	paciente3 = cPaciente(44743223,"amarillo",60,"en espera","12:30","paresia","12:45",2)
	paciente4 = cPaciente(22987359,"rojo",0,"atendido","15:30","politraumatismo","15:30",0)

	enfermero.set_estado()

	print("Hello World")

if __name__ == "__main__":
	main()
