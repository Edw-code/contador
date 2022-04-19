import tkinter
import random
ventana=tkinter.Tk()
#Titulo 1
ventana.title("contador")
ventana.geometry("400x300")
#Titulo 2
cont=tkinter.Label(ventana, text="Contador", font= "cambria 35")
cont.place(x=110, y=20)
#Contador numerico
nume=tkinter.Label(ventana, text= "0", font="cambria 45")
nume.place(x=190, y=90)

#Boton para aumentar
def sumar():
    valor = int(nume["text"])
    nume["text"]= f"{valor + 1}" 
    valor = int(nume["text"]) 
    cls(valor)

Aumentar=tkinter.Button(ventana, text="Aumentar", width=12, height=2, command=sumar, foreground="green" )
Aumentar.place(x=50, y=180)

#Boton resetear
def formatear():
    valor = int(nume["text"]) 
    nume["text"]= f"{valor *0 }" 
    valor = int(nume["text"]) 
    cls(valor)

Reset=tkinter.Button(ventana, text= "Reset", width=12, height=2, command=formatear )
Reset.place(x=160, y=180)

#Boton disminuir
def restar():
    valor = int(nume ["text"])
    nume["text"]= f"{valor -1 }"
    valor = int(nume["text"]) 
    cls(valor)

Disminuir=tkinter.Button(ventana, text= "Disminuir", width=12, height=2, command=restar, foreground="red")
Disminuir.place(x=270, y=180)

#Aplicar colores a los numeros
def cls(valor):
    if int(valor) < 0:
        nume.config(fg = "red")
    elif int(valor) == 0:
        nume.config(fg = "black")
    elif int(valor) > 0:
        nume.config(fg = "green")

ventana.mainloop()