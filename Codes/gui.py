# -*- coding: utf-8 -*-

import sys
from Tkinter import *

ventana = Tk()
ventana.geometry("656x426")
ventana.title("interfaz brazo")
imagenL=PhotoImage(file="Sin.gif")
lblimagen=Label(ventana,image=imagenL).place(x=0,y=0)

#definicion de la ventana

#ventana.grid(column=0, row=0, padx=(100,100), pady=(100,100))
#ventana.columnconfigure(0,weight=1)
#ventana.rowconfigure(0,weight=1)
#slider
q1 = Scale(ventana, from_=0, to=360, orient=HORIZONTAL)
q1.place(x=91,y=225)

q2 = Scale(ventana, from_=-50, to=200, orient=HORIZONTAL)
q2.place(x=91,y=265)
#
q3 = Scale(ventana, from_=-50, to=200, orient=HORIZONTAL)
q3.place(x=91,y=305)
#
q4 = Scale(ventana, from_=-90, to=90, orient=HORIZONTAL)
q4.place(x=91,y=345)
#

##Cuadros para introducir valores 
posx = ""
x1 = Entry(ventana, width=5, textvariable=posx)
x1.place(x=31,y=94)
#
posy = ""
y1 = Entry(ventana, width=5, textvariable=posy)
y1.place(x=71,y=94)
#
posz = ""
z1 = Entry(ventana, width=5, textvariable=posz)
z1.place(x=111,y=94)
ax1 = ""
ax2 = Entry(ventana, width=5, textvariable=ax1)
ax2.place(x=157,y=93)
#
#
ay1 = ""
ay2 = Entry(ventana, width=5, textvariable=ay1)
ay2.place(x=190,y=93)
#
#
az1 = ""
az2 = Entry(ventana, width=5, textvariable=az1)
az2.place(x=225,y=93)
#
##Botones
mover = Button(ventana, text="Start", width=5)
mover.place(x=22,y=112)
#
Para = Button(ventana, text="Stop", width=5)
Para.place(x=112,y=112)
#
ini = Button(ventana, text="Home", width=5)
ini.place(x=68,y=139)
#
##botones coche
#
automatico = Button(ventana, text="Traer agua",command = automatico width=10)
automatico.place(x=400,y=300)

automatico1 = Button(ventana, text="Traer medicación", width=15)
automatico1.place(x=500,y=300)

avanza = Button(ventana, text="Avanza", width=10)
avanza.place(x=448,y=64)
#
retro = Button(ventana, text="Retroceder", width=10)
retro.place(x=448,y=140)
#
girai = Button(ventana, text="Gira Izquierda", width=10)
girai.place(x=368,y=98)
#
Stop1 = Button(ventana, text="Stop", width=10)
Stop1.place(x=448,y=98)
#
girad = Button(ventana, text="Gira Derecha ", width=10)
girad.place(x=528,y=98)

ventana.mainloop()
