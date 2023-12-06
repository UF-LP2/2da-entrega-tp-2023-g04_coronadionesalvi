from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk 
from library.Enfermero import cEnfermero
from library.Medico import cMedico
from library.Hospital import cHospital
from library.Funciones import cargarMedicosCSV, cargarPacientesCSV
import tkinter as tk
from tkinter import Label, Button
from tkinter import Canvas 

listaPacientes = cargarPacientesCSV("pacientes.csv")
listaMedicos = cargarMedicosCSV("medicos.csv")
enfermeros = []
hospital = cHospital("Curitas", "Sarmiento 1853", listaPacientes, listaMedicos, enfermeros)



ventana = Tk()
ventana.geometry('800x600') # tamanyo en pixeles de la ventana
ventana.config(bg='dark slate gray') #asigno fondo blanco a la ventana
ventana.title('TRABAJO PRACTICO LABORATORIO DE PROGRAMACION 2')
etiqueta= Label(ventana, text='Hospital Curitas', fg='white', bg='dark slate grey', font='Verdana')
etiqueta.place(x=200, y= 10)

ventana2 =Tk()
ventana2.geometry('800x600')
ventana2.config(bg='dark slate gray')
ventana2.title('PACIENTES') 
etiqueta2= Label(ventana2, text='PACIENTES EN ESPERA', fg='white', bg='dark slate grey', font='Verdana')
etiqueta2.place(x=200, y= 10)

ventana3= Tk()
ventana3.geometry('800x600')
ventana3.config(bg='dark slate gray')
ventana3.title('MEDICOS') 
etiqueta3= Label(ventana3, text='MEDICOS', fg='white', bg='dark slate grey', font='Verdana')
etiqueta3.place(x=200, y= 10)


etiqueta5= Label(ventana, text='Contacto: curitas@gmail.com', fg='white', bg='dark slate grey', font='Verdana')
etiqueta5.place(x=50, y= 100)
etiqueta5= Label(ventana, text='Telefono de urgencia: 107', fg='white', bg='dark slate grey', font='Verdana')
etiqueta5.place(x=50, y= 140)
etiqueta5= Label(ventana, text='Direccion: Sarmiento 2134', fg='white', bg='dark slate grey', font='Verdana')
etiqueta5.place(x=50, y= 180)

text_lista = tk.Text(ventana2, height=100, width=100)
text_lista.pack()

text_lista2 = tk.Text(ventana3, height=100, width=100)
text_lista2.pack()

def imprimirListaPacientes(hospital: cHospital):
	lista = hospital.getPacientesString()  # Llama al método desde la instancia
	text_lista.delete("1.0", tk.END)  # Limpia el widget de texto
	text_lista.insert(tk.END, "\n\n".join(lista))

def imprimirListaMedicos(hospital: cHospital):
	lista = hospital.getMedicosString()   # Llama al método desde la instancia
	text_lista2.delete("1.0", tk.END)  # Limpia el widget de texto
	text_lista2.insert(tk.END, "\n\n".join(lista))

boton= Button(ventana, text='Mostrar sala de espera', fg='black', font='Verdana',command = imprimirListaPacientes(hospital))
boton7= Button(ventana, text='Mostrar lista de medicos', fg='black', font='Verdana',command= imprimirListaMedicos(hospital))
boton8= Button(ventana, text='Actualizar sala de espera', fg='black', font='Verdana',command=0)


#ubicacion de los botones 

boton.place(x= 50, y= 240)
boton7.place(x=50, y=290)
boton8.place(x=50, y=340)

ventana.mainloop() # método que mantiene 24/7 activa a la ventana