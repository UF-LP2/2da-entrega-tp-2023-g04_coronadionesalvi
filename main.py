from datetime import datetime, time
from library.Enfermero import cEnfermero
from library.Hospital import cHospital
from library.Medico import cMedico
from library.Paciente import cPaciente



def main() -> None:
	pacientes = [paciente1,paciente2,paciente3,paciente4]
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

	paciente1 = cPaciente(53253455,"azul",240,"en espera",time(11,50),"sin urgencia",time(14,50),4)
	paciente2 = cPaciente(46246454,"azul",240,"en espera",time(10,40),"sin urgencia",time(14,50),4)
	paciente3 = cPaciente(46464443,"azul",240,"en espera",time(11,30),"sin urgencia",time(13,30),4)
	paciente4 = cPaciente(43546674,"azul",240,"en espera",time(11,50),"sin urgencia",time(15,30),4)
	paciente5 = cPaciente(25235434,"azul",240,"en espera",time(15,50),"sin urgencia",time(13,50),4)

	paciente6 = cPaciente(44000234,"rojo",0,"en espera",time(6,50),"politraumatismo",time(6,50),0)
	paciente7 = cPaciente(43400892,"rojo",0,"en espera",time(8,50),"politraumatismo",time(8,50),0)
	paciente8 = cPaciente(22907654,"rojo",0,"atendido",time(7,30),"politraumatismo",time(7,30),0)
	paciente9 = cPaciente(23337654,"rojo",0,"atendido",time(13,40),"politraumatismo",time(13,40),0)
	paciente10 = cPaciente(44577798,"rojo",0,"en espera",time(13,50),"politraumatismo",time(13,50),0)

	paciente11 = cPaciente(44565234,"amarillo",60,"en espera",time(18,50),"paresia",time(19,50),2)
	paciente12 = cPaciente(44565234,"amarillo",60,"en espera",time(19,50),"paresia",time(20,40),2)
	paciente13 = cPaciente(22907654,"amarillo",60,"atendido",time(13,50),"paresia",time(14,50),2)
	paciente14 = cPaciente(44056734,"amarillo",60,"atendido",time(11,50),"paresia",time(12,50),2)
	paciente15 = cPaciente(12345678,"amarillo",60,"en espera",time(13,50),"paresia",time(14,10),2)

	paciente16 = cPaciente(22489300,"verde",120 ,"en espera",time(13,10),"odontalgias",time(13,50),3)
	paciente17 = cPaciente(34563454,"verde",120 ,"atendido",time(12,15),"odontalgias",time(13,20),3)
	paciente18 = cPaciente(22456789,"verde",120 ,"en espera",time(8,55),"odontalgias",time(9,30),3)
	paciente19 = cPaciente(23456455,"verde",120 ,"en espera",time(13,20),"odontalgias",time(13,50),3)
	paciente20 = cPaciente(23456789,"verde",120 ,"en espera",time(17,50),"odontalgias",time(18,40),3)
	
	enfermero.set_estado()

	print("Hello World")

if __name__ == "__main__":
	main()


