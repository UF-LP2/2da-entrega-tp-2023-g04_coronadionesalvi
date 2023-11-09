from library.Enfermero import cEnfermero
from library.Hospital import cHospital
from library.Medico import cMedico
from library.Paciente import cPaciente



def main() -> None:
	enfermero = cEnfermero(43567555,"noche",False,False)
	enfermero2 = cEnfermero(23765654,"tarde",False,False)
	enfermero3 = cEnfermero(23223456,"maniana",True, False)
	enfermero4 = cEnfermero(34574654,"noche",False, True)
	
	medico = cMedico(3254365)
	medico1 = cMedico(4325211)
	medico2 = cMedico(123513)
	medico4 = cMedico(324652)

	paciente = cPaciente(44787654,"verde",120,"en espera","15:30","esguince","16:30",3)
	paciente2 = cPaciente(44787654,"verde",120,"en espera","15:30","esguince","16:30",3)
	paciente3 = cPaciente(44787654,"verde",120,"en espera","15:30","esguince","16:30",3)
	paciente4 = cPaciente(44787654,"verde",120,"en espera","15:30","esguince","16:30",3)

	enfermero.set_estado()

	print("Hello World")

if __name__ == "__main__":
	main()
