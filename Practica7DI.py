import tkinter as tk
from tkinter import ttk

def deseleccionar(var,opciones):
    for opcion in opciones:
        if opcion != var:
            opcion.set("")
def copiar():
    nombre2.delete(0,tk.END)
    nombre2.insert(0,nombre.get())

raiz=tk.Tk()

raiz.geometry("1000x800")

raiz.configure(background='white')

estilo=ttk.Style()
estilo.theme_use('clam')
estilo.configure('TLabel',foreground='green',font=('Arial',15),background='white')
estilo.configure('TRadiobutton',background='white')

titulo = ttk.Label(raiz, text="DATOS DE ENVÍO").grid(row=0,column=1,padx=25,pady=10)

#Nombre y cif
ttk.Label(raiz, text="NOMBRE Y APELLIDOS").grid(row=1,column=0,padx=50,pady=10)
nombre=ttk.Entry(raiz,width=30)
nombre.grid(row=2,column=0,padx=25,pady=10)
ttk.Label(raiz, text="CIF").grid(row=1,column=1,padx=25,pady=10)
apellidos=ttk.Entry(raiz,width=30).grid(row=2,column=1,padx=25,pady=10)

#Direcciones
ttk.Label(raiz, text="DIRECCION").grid(row=3,column=0,padx=25,pady=30)
direccion=ttk.Entry(raiz,width=30).grid(row=4,column=0,padx=25,pady=10)
ttk.Label(raiz, text="CÓDIGO POSTAL").grid(row=3,column=1,padx=25,pady=10)
codigo=ttk.Entry(raiz,width=30).grid(row=4,column=1,padx=25,pady=10)
ttk.Label(raiz, text="PROVINCIA").grid(row=3,column=2,padx=25,pady=30)
provincia=ttk.Entry(raiz,width=30).grid(row=4,column=2,padx=25,pady=10)

#Opcion de envio
eleccion1=tk.StringVar()
eleccion2=tk.StringVar()
eleccion3=tk.StringVar()

ttk.Label(raiz, text="MÉTODO DE ENVÍO").grid(row=5,column=0,padx=25,pady=30)
ttk.Radiobutton(raiz,text="Correos Express",variable=eleccion1,command=lambda:deseleccionar(eleccion1,[eleccion2,eleccion3])).grid(row=6,column=0,padx=25,pady=10)
ttk.Radiobutton(raiz,text="MRW",variable=eleccion2,command=lambda:deseleccionar(eleccion2,[eleccion1,eleccion3])).grid(row=6,column=1,padx=10,pady=10)
ttk.Radiobutton(raiz,text="SEUR",variable=eleccion3,command=lambda:deseleccionar(eleccion3,[eleccion1,eleccion2])).grid(row=6,column=2,padx=10,pady=10)                                                 


titulo = ttk.Label(raiz, text="DATOS DE FACTURACIÓN").grid(row=7,column=1,padx=25,pady=10)
ttk.Button(raiz,text="MISMOS DATOS",command=copiar).grid(row=7,column=2,padx=25,pady=10)

#Nombre y cif
ttk.Label(raiz, text="NOMBRE Y APELLIDOS").grid(row=8,column=0,padx=50,pady=10)
nombre2=ttk.Entry(raiz,width=30)
nombre2.grid(row=9,column=0,padx=25,pady=10)
ttk.Label(raiz, text="CIF").grid(row=8,column=1,padx=25,pady=10)
apellidos2=ttk.Entry(raiz,width=30).grid(row=9,column=1,padx=25,pady=10)

#Direcciones
ttk.Label(raiz, text="DIRECCION").grid(row=10,column=0,padx=25,pady=30)
direccion=ttk.Entry(raiz,width=30).grid(row=11,column=0,padx=25,pady=10)
ttk.Label(raiz, text="CÓDIGO POSTAL").grid(row=10,column=1,padx=25,pady=10)
codigo=ttk.Entry(raiz,width=30).grid(row=11,column=1,padx=25,pady=10)
ttk.Label(raiz, text="PROVINCIA").grid(row=10,column=2,padx=25,pady=30)
provincia=ttk.Entry(raiz,width=30).grid(row=11,column=2,padx=25,pady=10)

raiz.mainloop()
