import tkinter as tk
import mysql.connector 
import re
from mysql.connector import Error
from cgitb import text
from logging import root
from tokenize import String
from turtle import width
from tkinter import Canvas, messagebox, filedialog
from tkinter import messagebox, Tk, Entry, Toplevel

nombre = ""
apellido = ""
edad = ""
estatura = ""
telefono = ""
width = 600
height = 750

def conectar_bd():
    try:
        conexion = mysql.connector.connect(



            host = "localhost",
            user = "root",
            password = "#Sincodigo1",
            database = "programacionavanzada"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")

conexion = conectar_bd()

def insertar_datos(conexion, nombre, apellidos, telefono, edad, estatura, genero):
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO registros (nombre, apellidos, telefono, edad, estatura, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nombre, apellidos, telefono, edad, estatura, genero)
        cursor.execute(query, values)
        conexion.commit()
        show_message_box()
        print("Datos guardadas con exito")
    except Error as e:
        print(f"Error al insertar datos: {e}")



def cerrar_conexion():
    conexion.close()


def validar_numero(input):
    pattern = r"^\d{0,10}$"
    return bool(re.match(pattern, input))

def detectar_DifLetras(event):
    tecla = event.keysym

    if tecla.isalpha() or tecla == 'space' or tecla == 'BackSpace':
        return
    else:
        messagebox.showwarning("Advertencia", "Solo se permiten letras")
        

def detectar_DifNumeros(event):
    tecla = event.keysym

    if tecla.isdigit() or tecla == 'space' or tecla == 'BackSpace':
        return
    else:
        messagebox.showwarning("Advertencia", "Solo se permiten numeros")
        return "break"

def limpiar_campos():
    tb_nombre.delete(0, tk.END)
    tb_apelllido.delete(0, tk.END)
    tb_telefono.delete(0, tk.END)
    tb_edad.delete(0, tk.END)
    tb_estatura.delete(0, tk.END)
    genero_var.set(None)

    
def borrar_fun():
    limpiar_campos()

def get_entry_values():
    nombre = tb_nombre.get()
    apellido = tb_apelllido.get()
    edad = tb_edad.get()
    estatura = tb_estatura.get()
    telefono = tb_telefono.get()
    genero = genero_var.get()

    insertar_datos(conexion, nombre, apellido, telefono, edad, estatura, genero)



    """ ruta_archivo =  filedialog.asksaveasfilename(defaultextension=".txt", 
                                                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
                                                title="Guardar archivo")
    
    if ruta_archivo:

        with open(ruta_archivo, "w") as archivo:
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Apellido: {apellido}\n")
            archivo.write(f"Teléfono: {telefono}\n")
            archivo.write(f"Edad: {edad}\n")
            archivo.write(f"Estatura: {estatura}\n")
            archivo.write(f"Género: {genero}\n")

        messagebox.showinfo("Datos guardados", f"Los datos han sido guardados exitosamente en {ruta_archivo}.")
     """
    #Cambiar el valor de un label
    #lb_apellido.config(text=nombre)
    
def show_message_box():
    messagebox.showinfo("Informacion", "Datos Guardados con exito \n\n" )

def crear_degradado(canvas, color1, color2):
    ancho = canvas.winfo_width()
    alto = canvas.winfo_height()
    for i in range(ancho):
        color = f'#{int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // ancho:02x}' \
                f'{int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // ancho:02x}' \
                f'{int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // ancho:02x}'
        canvas.create_line(i, 0, i, alto, fill=color)
        
# Obtener el tamaño de la pantalla
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()

# Calcular la posición x, y
#x = (screen_width // 2) - (width // 2)
#y = (screen_height // 2) - (height // 2)

root = tk.Tk()
root.geometry(f"{width}x{height}")
root.title("Formulario")

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack(fill="both", expand=True)

canvas.bind("<Configure>", lambda e: crear_degradado(canvas, "#FF5733", "#33FF57"))

p1 = tk.Frame(canvas, bg="#FFFAFA", width=400, height=650)
canvas.create_window(300, 380, window=p1)

#Titulo
lb_registro = tk.Label(p1,text= "REGISTRO", font=("Arial", 24))
lb_registro.place(x=120, y=10)
    
#Nombre
lb_nombre = tk.Label(p1, text = "Nombre")
lb_nombre.place(x=30, y=70)

#Nombre
tb_nombre = tk.Entry(p1)
tb_nombre.place(x=100, y=70)

tb_nombre.bind("<Key>", detectar_DifLetras)


#Apellido
lb_apellido = tk.Label(p1, text = "Apellido")
lb_apellido.place(x=30, y=100)

tb_apelllido = tk.Entry(p1)
tb_apelllido.place(x = 100, y = 100)

tb_apelllido.bind("<Key>", detectar_DifLetras)

#Telefono
lb_telefono = tk.Label(p1, text = "Telefono")
lb_telefono.place(x = 30, y = 140)

tb_telefono = tk.Entry(p1)
tb_telefono.place(x = 100, y = 140)

tb_telefono.config(validate="key", validatecommand=(p1.register(validar_numero), "%P"))

tb_telefono.bind("<Key>", detectar_DifNumeros)

#Edad
lb_edad = tk.Label(p1, text=("Edad"))
lb_edad.place(x = 30, y = 180)

tb_edad = tk.Entry(p1)
tb_edad.place(x = 100, y = 180 )

tb_edad.bind("<Key>", detectar_DifNumeros)

#Estatura
lb_estatura = tk.Label(p1, text="Estatura")
lb_estatura.place(x = 30, y = 220)

tb_estatura = tk.Entry(p1)
tb_estatura.place(x = 100, y = 220)

tb_estatura.bind("<Key>", detectar_DifNumeros)

#Genero
lb_genero = tk.Label(p1, text="Genero")
lb_genero.place(x = 30, y = 260)

genero_var = tk.StringVar()
genero_var.set(None)

#RadionButton Hombre
rb_genero_hombre = tk.Radiobutton(p1, text="Hombre", variable=genero_var, value="Hombre")
rb_genero_hombre.place(x = 90, y = 260 )


#RadioButton Mujer
rb_genero_mujer = tk.Radiobutton(p1, text="Mujer", variable=genero_var, value="Mujer")
rb_genero_mujer.place(x = 190, y = 260)

#Boton Aceptar
btn_guardar = tk.Button(p1, text=("Guardar"), command=get_entry_values)
btn_guardar.place(x = 80, y = 300)

#Boton Cancelar
btn_cancelar = tk.Button(p1, text=("Cancelar"), command=limpiar_campos)
btn_cancelar.place(x = 260, y = 300)



root.mainloop()

