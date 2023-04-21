import tkinter as tk
from tkinter import messagebox
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from math import log

root = Tk()
root.geometry("1000x700")
root.title("Graficador")
root.configure(bg="#87CEEB")
fig, ax = plt.subplots()

def graficar():
    global xi
    global xu
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    d = float(d_entry.get())
    desde = float(desde_entry.get())
    hasta = float(hasta_entry.get())
    

    funcion = opcion_funcion.get()

    ax.clear()
    ax.grid(TRUE)
    x = np.linspace(desde, hasta, num=1000)

    z = 1
    i = 0


    if funcion == 1:
        while i < 20:
            mas = z-( a * z +b)/a
            z = mas
            i += 1
        y = a * x + b + c + d
        Raiz.config(text=f'La raiz es = {mas} ')

    elif funcion == 2:
        while i < 20:
            mas = z-(a *z ** 2 + b * z + c)/(2*a*z+b)
            z = mas
            i += 1
        y = a * x ** 2 + b * x + c
        Raiz.config(text=f'La raiz es = {mas} ')

    elif funcion == 3:
        while i < 20:
            mas = z- (a * z ** 3 + b * z ** 2 + c * z + d)/(3*a * z ** 2 + 2*b * z  + c )
            z = mas
            i += 1
        y = a * x ** 3 + b * x ** 2 + c * x + d
        Raiz.config(text=f'La raiz es = {z} ')

    else:
        if b!=0 and c<0:
          while i < 40:
            mas = z-((pow(a, b*z)+c)/(b*pow(a,b*z)*log(a)))
            z = mas
            i += 1
        else:
            z=0
        y = pow(a, b*x) + c
        Raiz.config(text=f'La raiz es = {z} ')

    ax.plot(x, y)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    canvas.draw()

frame = Frame(root)
frame.pack()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(TRUE)


titulo = Label(frame, text="Graficador",font=("Roboto",22))
titulo.pack(padx=10, pady=10, side=TOP)

columna_izquierda = Frame(frame)
columna_izquierda.pack(side=LEFT)

opcion_funcion = IntVar()
opcion_funcion.set(1)
funcion_label = Label(columna_izquierda, text="Función:")
funcion_label.pack(pady=8, padx=10)
lineal_radio = Radiobutton(columna_izquierda, text="Lineal", variable=opcion_funcion, value=1)
lineal_radio.pack(pady=8, padx=10)
cuadratica_radio = Radiobutton(columna_izquierda, text="Cuadrática", variable=opcion_funcion, value=2)
cuadratica_radio.pack(pady=8, padx=10)
cubica_radio = Radiobutton(columna_izquierda, text="Cúbica", variable=opcion_funcion, value=3)
cubica_radio.pack(pady=8, padx=12)
Exponencial_radio = Radiobutton(columna_izquierda, text="Exponencial", variable=opcion_funcion, value=4)
Exponencial_radio.pack(pady=8, padx=12)



a_label = Label(columna_izquierda, text="a:")
a_label.pack(pady=8, padx=10)
a_entry = Entry(columna_izquierda)
a_entry.pack(pady=8, padx=10)

b_label = Label(columna_izquierda, text="b:")
b_label.pack(pady=8, padx=10)
b_entry = Entry(columna_izquierda)
b_entry.pack(pady=8, padx=10)

c_label = Label(columna_izquierda, text="c:")
c_label.pack(pady=8, padx=10)
c_entry = Entry(columna_izquierda)
c_entry.pack(pady=8, padx=10)

d_label = Label(columna_izquierda, text="d:")
d_label.pack(pady=8, padx=10)
d_entry = Entry(columna_izquierda)
d_entry.pack(pady=8, padx=10)

desde_label = Label(columna_izquierda, text="Desde:")
desde_label.pack(pady=8, padx=10)
desde_entry = Entry(columna_izquierda)
desde_entry.pack(pady=8, padx=13)

hasta_label = Label(columna_izquierda, text="Hasta:")
hasta_label.pack(pady=8, padx=10)
hasta_entry = Entry(columna_izquierda)
hasta_entry.pack(pady=8, padx=10)

Raiz = Label(frame, text="", font=("Roboto",10))
Raiz.pack(padx=10, pady=10)

botonGraficar = Button(frame, text="Graficar", command=graficar)
botonGraficar.pack(pady=5, padx=12)


canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH)

root.mainloop()