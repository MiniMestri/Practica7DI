import tkinter as tk
from tkinter import ttk
import json

def copiar():
    entry_nombre_factura.insert(0,entry_nombre.get())
    
    entry_apellidos_factura.insert(0,entry_apellidos.get())

    entry_direccion_factura.insert(0,entry_direccion.get())

    entry_cp_factura.insert(0,entry_cp.get())

    entry_provincia_factura.insert(0,entry_provincia.get())

def confirmacion(evento):
    ventana_confirmacion = tk.Toplevel(raiz, padx=60,pady=60)
    ventana_confirmacion.title("Registro OK")

    mensaje_confirmacion = ttk.Label(ventana_confirmacion,text="Registro exitoso", font=('Arial',15,))
    mensaje_confirmacion.pack(padx=10,pady=10)

    boton_cerrar = ttk.Button(ventana_confirmacion, text="Cerrar", command=ventana_confirmacion.destroy)
    boton_cerrar.pack(pady=10)

def borrar():
    entry_nombre.delete(0,tk.END)
    entry_nombre_factura.delete(0,tk.END)

    entry_apellidos.delete(0,tk.END)
    entry_apellidos_factura.delete(0,tk.END)

    entry_direccion.delete(0,tk.END)
    entry_direccion_factura.delete(0,tk.END)

    entry_cp.delete(0,tk.END)
    entry_cp_factura.delete(0,tk.END)
    
    entry_provincia.delete(0,tk.END)
    entry_provincia_factura.delete(0,tk.END)

def registrar():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    direccion = entry_direccion.get()
    cp = entry_cp.get()
    provincia = entry_provincia.get()
    eleccion_envio = eleccion_var.get()

    nombre_factura = entry_nombre.get()
    apellidos_factura = entry_apellidos.get()
    direccion_factura = entry_direccion.get()
    cp_factura = entry_cp.get()
    provincia_factura = entry_provincia.get()

    datos = {
        'nombre': nombre,
        'apellidos': apellidos,
        'direccion': direccion,
        'cp': cp,
        'provincia': provincia,
        'metodo_envio': eleccion_envio,
        'nombre_factura': nombre_factura,
        'apellidos_factura': apellidos_factura,
        'direccion_factura': direccion_factura,
        'cp_factura': cp_factura,
        'provincia_factura': provincia_factura,
    }
    datos_json=json.dumps(datos,indent=2)

    archivo=open("C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\DESARROLLO DE INTERFACES\\Practicas\\Practica7DI\\bbdd.json","w")
    archivo.write(datos_json)
    archivo.close()
    
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
eleccion_var=tk.StringVar()

ttk.Label(raiz, text="MÉTODO DE ENVÍO").grid(row=5,column=0,padx=25,pady=30)

ttk.Radiobutton(raiz,text="Correos Express",variable=eleccion_var,value="Correos Express").grid(row=6,column=0,padx=25,pady=10)
ttk.Radiobutton(raiz,text="MRW",variable=eleccion_var,value="MRW").grid(row=6,column=1,padx=10,pady=10)
ttk.Radiobutton(raiz,text="SEUR",variable=eleccion_var,value="SEUR").grid(row=6,column=2,padx=10,pady=10)                                                 

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
boton_mismos_datos=ttk.Button(raiz,text="MISMOS DATOS",command=copiar)
boton_mismos_datos.grid(row=7,column=2,padx=25,pady=10)
boton_borrar=ttk.Button(raiz,text="BORRAR",command=borrar).grid(row=12,column=2,padx=25,pady=10)
boton_registrar=ttk.Button(raiz,text="REGISTRAR",command=registrar).grid(row=12,column=1,padx=25,pady=10)
boton_mismos_datos.bind("<Button-1>",confirmacion)

raiz.mainloop()
