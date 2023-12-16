import tkinter as tk
from tkinter import ttk

def copiar():
    entry_nombre_factura.insert(0,entry_nombre.get())
    
    entry_apellidos_factura.insert(0,entry_apellidos.get())

    entry_direccion_factura.insert(0,entry_direccion.get())

    entry_cp_factura.insert(0,entry_cp.get())

    entry_provincia_factura.insert(0,entry_provincia.get())

def confirmacion(evento):
    ventana_confirmacion = tk.Toplevel(raiz, padx=50,pady=50)
    ventana_confirmacion.title("Formulario de registro")

    mensaje_confirmacion = ttk.Label(ventana_confirmacion,text="Registrado con éxito", font=('Arial',15))
    mensaje_confirmacion.pack(padx=10,pady=10)

    boton_cerrar = ttk.Button(ventana_confirmacion, text="Cerrar", command=ventana_confirmacion.destroy)
    boton_cerrar.pack(pady=10)

raiz=tk.Tk()

raiz.geometry("1000x800")

raiz.configure(background='white')

estilo=ttk.Style()
estilo.theme_use('clam')
estilo.configure('TLabel',foreground='green',font=('Arial',15),background='white')
estilo.configure('TRadiobutton',background='white')

#DATOS DE ENVIO
titulo = ttk.Label(raiz, text="DATOS DE ENVÍO").grid(row=0,column=1,padx=25,pady=10)

#Introducción de nombre y apellidos
ttk.Label(raiz, text="NOMBRE Y APELLIDOS").grid(row=1,column=0,padx=50,pady=10)
entry_nombre=ttk.Entry(raiz,width=30)
entry_nombre.grid(row=2,column=0,padx=25,pady=10)

ttk.Label(raiz, text="CIF").grid(row=1,column=1,padx=25,pady=10)
entry_apellidos=ttk.Entry(raiz,width=30)
entry_apellidos.grid(row=2,column=1,padx=25,pady=10)

#Introducción de dirección de envío
ttk.Label(raiz, text="DIRECCION").grid(row=3,column=0,padx=25,pady=30)
entry_direccion=ttk.Entry(raiz,width=30)
entry_direccion.grid(row=4,column=0,padx=25,pady=10)

ttk.Label(raiz, text="CÓDIGO POSTAL").grid(row=3,column=1,padx=25,pady=10)
entry_cp=ttk.Entry(raiz,width=30)
entry_cp.grid(row=4,column=1,padx=25,pady=10)

ttk.Label(raiz, text="PROVINCIA").grid(row=3,column=2,padx=25,pady=30)
entry_provincia=ttk.Entry(raiz,width=30)
entry_provincia.grid(row=4,column=2,padx=25,pady=10)

#Opcion de envio
eleccion=tk.StringVar()

ttk.Label(raiz, text="MÉTODO DE ENVÍO").grid(row=5,column=0,padx=25,pady=30)

ttk.Radiobutton(raiz,text="Correos Express",variable=eleccion,value="Correos Express").grid(row=6,column=0,padx=25,pady=10)
ttk.Radiobutton(raiz,text="MRW",variable=eleccion,value="MRW").grid(row=6,column=1,padx=10,pady=10)
ttk.Radiobutton(raiz,text="SEUR",variable=eleccion,value="SEUR").grid(row=6,column=2,padx=10,pady=10)                                                 

#DATOS DE FACTURACIÓN
titulo = ttk.Label(raiz, text="DATOS DE FACTURACIÓN").grid(row=7,column=1,padx=25,pady=10)

#Nombre y cif
ttk.Label(raiz, text="NOMBRE Y APELLIDOS").grid(row=8,column=0,padx=50,pady=10)
entry_nombre_factura=ttk.Entry(raiz,width=30)
entry_nombre_factura.grid(row=9,column=0,padx=25,pady=10)

ttk.Label(raiz, text="CIF").grid(row=8,column=1,padx=25,pady=10)
entry_apellidos_factura=ttk.Entry(raiz,width=30)
entry_apellidos_factura.grid(row=9,column=1,padx=25,pady=10)

#Direcciones
ttk.Label(raiz, text="DIRECCION").grid(row=10,column=0,padx=25,pady=30)
entry_direccion_factura=ttk.Entry(raiz,width=30)
entry_direccion_factura.grid(row=11,column=0,padx=25,pady=10)

ttk.Label(raiz, text="CÓDIGO POSTAL").grid(row=10,column=1,padx=25,pady=10)
entry_cp_factura=ttk.Entry(raiz,width=30)
entry_cp_factura.grid(row=11,column=1,padx=25,pady=10)

ttk.Label(raiz, text="PROVINCIA").grid(row=10,column=2,padx=25,pady=30)
entry_provincia_factura=ttk.Entry(raiz,width=30)
entry_provincia_factura.grid(row=11,column=2,padx=25,pady=10)

#Botones
boton=ttk.Button(raiz,text="MISMOS DATOS",command=copiar).grid(row=7,column=2,padx=25,pady=10)
boton.bind("<Button-1>",confirmacion)

raiz.mainloop()
