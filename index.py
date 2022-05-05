import tkinter
from cProfile import label
from tkinter import *
from tkinter import ttk


class alumno:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("hola mundo")
        marco=LabelFrame(self.ventana,text="alumno")
        marco.grid(row=0,column=0,columnspan=3,pady=20)
        #nombre
        Label(self.ventana,text="nombre").grid(row=0,column=0)
        Entry(self.ventana).grid(row=0,column=1)
        #clave
        Label(self.ventana,text="clave").grid(row=1,column=0)
        Entry(self.ventana).grid(row=1,column=1)
        #boton
        ttk.Button(self.ventana,text="guardar alumno").grid(row=2,columnspan=2,sticky=W+E)

if __name__ == "__main__":
    ventana=Tk()
    aplicacion=alumno(ventana)
    ventana.mainloop()
