from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
#from library.Hospital import cHospital


ventana = Tk()
ventana.config(bg='PaleGreen1')
ventana.geometry('800x600') #tam en pixeles
ventana.title('Trabajo Practico Final - Laboratorio de Programación 2')
etiqueta= Label(ventana, text = 'Hospital Curitas', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=180, y= 10) #ubicacion en pantalla

etiqueta= Label(ventana, text = 'CONTACTO', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=50, y= 70)
etiqueta= Label(ventana, text = '4799-5692', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=50, y= 120)

boton1= Button(ventana, text='Lista de pacientes', fg='black', font='Verdana')
#boton2= Button(ventana, text='CONTACTOS',bg='white', fg='black', font='Verdana')

boton5= Button(ventana, text='Normal', bg='bisque4',fg='black', font='Verdana')
boton6= Button(ventana, text='No urgente', bg='bisque4', fg='black',font='Verdana')

#poimage_image_1 = PhotoImage('imginicio.gif')
#Label(ventana, image = image_image_1).place(x=50, y=500)

boton1.place(x=50, y= 70)
#boton2.place(x= 50, y= 120)

#boton4.place(x= 50, y= 220)
boton5.place(x= 50, y= 270)
boton6.place(x= 50, y= 320)


ventana.mainloop()
