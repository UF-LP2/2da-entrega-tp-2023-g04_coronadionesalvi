from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk

ventana = Tk()
ventana.config(bg='green')
ventana.geometry('800x600') #tam en pixeles
ventana.title('Trabajo Practico Final - Laboratorio de Programación 2')
etiqueta= Label(ventana, text = 'Hospital Curitas', fg='black', bg='white', font='Verdana')
etiqueta.place(x=180, y= 10) #ubicacion en pantalla


boton= Button(ventana, text='Lista de pacientes', fg='black', font='Verdana')
boton2= Button(ventana, text='Riesgo vital',bg='bisque4', fg='black', font='Verdana')
boton3= Button(ventana, text='Urgencia alta', bg='bisque4', fg='black',font='Verdana')
boton4= Button(ventana, text='Urgencia Media', bg='bisque4', fg='black',font='Verdana')
boton5= Button(ventana, text='Normal', bg='bisque4',fg='black', font='Verdana')
boton6= Button(ventana, text='No urgente', bg='bisque4', fg='black',font='Verdana')

boton.place(x=50, y= 70)
boton2.place(x= 50, y= 120)
boton3.place(x= 50, y= 170)
boton4.place(x= 50, y= 220)
boton5.place(x= 50, y= 270)
boton6.place(x= 50, y= 320)


ventana.mainloop()
