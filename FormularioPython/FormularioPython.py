from cgitb import text
from logging import root
import tkinter as tk
from tokenize import String
from turtle import width
from tkinter import Canvas, messagebox

nombre = ""
apellido = ""
edad = ""
estatura = ""
telefono = ""

def limpiar_campos():
    tb_nombre.delete(0,tk.End)
    tb_apelllido.delete(0,tk.End)
    tb_edad.delete(0,tk.End)
    tb_telefono.delete(0,tk.End)
    
def borrar_fun():
    limpiar_campos()

def get_entry_values():
    nombre = tb_nombre.get()
    apellido = tb_apelllido.get()
    edad = tb_edad.get()
    estatura = tb_estatura.get()
    telefono = tb_telefono.get()

    messagebox.showinfo("Informacion", "Datos Guardados con exito: \n\n" + datos)
    
    #Cambiar el valor de un label
    #lb_apellido.config(text=nombre)
    
def show_message_box():
    messagebox.showinfo("Informacion", "Datos Guardados con exito: \n\n" + datos)

def crear_degradado(canvas, color1, color2):
    ancho = canvas.winfo_width()
    alto = canvas.winfo_height()
    for i in range(ancho):
        color = f'#{int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // ancho:02x}' \
                f'{int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // ancho:02x}' \
                f'{int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // ancho:02x}'
        canvas.create_line(i, 0, i, alto, fill=color)

root = tk.Tk()
root.geometry("500x900")
root.title("Formulario")

canvas = tk.Canvas(root, width=500, height=900)
canvas.pack(fill="both", expand=True, ipady= 40, ipadx=40)

canvas.bind("<Configure>", lambda e: crear_degradado(canvas, "#FF5733", "#33FF57"))

p1 = tk.Frame(canvas, bg="#874638", width = 400, height = 800)
p1.pack(fill = "both", expand = False, ipady= 40, ipadx=40)

lb_nombre = tk.Label(p1, text = "Hola")
lb_nombre.place(x=30, y=20)

tb_nombre = tk.Entry(p1)
tb_nombre.place(x= 100, y=20)

lb_apellido = tk.Label(p1, text = "Apellido")
lb_apellido.place(x=30, y=60)

tb_apelllido = tk.Entry(p1)
tb_apelllido.place(x = 100, y = 60)

lb_telefono = tk.Label(p1, text = "Telefono")
lb_telefono.place(x = 30, y = 100)

tb_telefono = tk.Entry(p1)
tb_telefono.place(x = 100, y = 100)

lb_edad = tk.Label(p1, text=("Edad"))
lb_edad.place(x = 30, y = 140)

tb_edad = tk.Entry(p1)
tb_edad.place(x = 100, y = 140 )

lb_estatura = tk.Label(p1, text="Estatura")
lb_estatura.place(x = 30, y = 180)

tb_estatura = tk.Entry(p1)
tb_estatura.place(x = 100, y = 180)

lb_genero = tk.Label(p1, text="Genero")
lb_genero.place(x = 30, y = 220)

rb_genero_hombre = tk.Radiobutton()
rb_genero_hombre.place(x = 90, y = 220 )

rb_genero_mujer = tk.Radiobutton()
rb_genero_mujer.place(x = 140, y = 220)

btn_aceptar = tk.Button(p1, text=("Aceptar"), command=get_entry_values)
btn_aceptar.place(x = 150, y = 280)





datos = "Nombres" + nombre  +  "\n" + "Apellidos" + apellido + "\n" + "Edad" + edad + "anos\n" + "Estatura" + estatura + "\n" + "Telefonos: " +  telefono + "\n"
#+ "Genero" + genero + "\n"


root.mainloop()

