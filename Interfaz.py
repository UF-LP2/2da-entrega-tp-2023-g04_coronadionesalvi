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

#etiqueta= Label(ventana, text = 'CONTACTO', fg='black', bg='PaleGreen1', font='Verdana')
#etiqueta.place(x=50, y= 70)
etiqueta= Label(ventana, text = '4799-5692', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=50, y= 100)
etiqueta= Label(ventana, text = 'Vicente Fidel Lopez 748', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=50, y= 440)
etiqueta= Label(ventana, text = 'Direccion', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=50, y= 400)
etiqueta= Label(ventana, text = 'Contacto', fg='black', bg='PaleGreen1', font='Verdana')
etiqueta.place(x=50, y= 70)


#boton1 = Button(ventana, text='Contactos', fg='Black', font='Verdana')
#boton2= Button(ventana, text='CONTACTOS',bg='white', fg='black', font='Verdana')

boton5= Button(ventana, text='Lista de pacientes', bg='bisque4',fg='white', font='Verdana')
boton6= Button(ventana, text='Lista de enfermeros', bg='bisque4',fg='white', font='Verdana')
boton7= Button(ventana, text='Lista de medicos', bg='bisque4',fg='white', font='Verdana')
boton8= Button(ventana, text='Urgencia', bg='bisque4',fg='white', font='Verdana')
#boton6= Button(ventana, text='Direccion', bg='bisque4', fg='black',font='Verdana')

#poimage_image_1 = PhotoImage('imginicio.gif')
#Label(ventana, image = image_image_1).place(x=50, y=500)

#boton1.place(x=50, y= 70)
#boton2.place(x= 50, y= 120)

#boton4.place(x= 50, y= 220)
boton5.place(x= 50, y= 230)
boton6.place(x= 50, y= 280)
boton7.place(x= 50, y= 330)
boton8.place(x= 50, y= 140)
#boton6.place(x= 50, y= 320)


ventana.mainloop()
