from cgitb import text
from logging import root
import tkinter as tk
from turtle import width

def crear_degradado(canvas, color1, color2):
    ancho = canvas.winfo_width()
    alto = canvas.winfo_height()
    for i in range(ancho):
        color = f'#{int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // ancho:02x}' \
                f'{int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // ancho:02x}' \
                f'{int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // ancho:02x}'
        canvas.create_line(i, 0, i, alto, fill=color)

root = tk.Tk()
root.geometry("800x500")
root.title("Formulario")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

canvas.bind("<Configure>", lambda e: crear_degradado(canvas, "#FF5733", "#33FF57"))

p1 = tk.Frame(master=p1, bg="#874638", width = 500, height = 900)
p1.pack(fill = "both", expand = True)

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

root.mainloop()

