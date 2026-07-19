import tkinter as tk

texto_mostrar = "0"

def mostrar_numero(x):
    global texto_mostrar
    if texto_mostrar == "0":
        texto_mostrar = f"{x}"
    else:
        texto_mostrar += f"{x}"
    actualizar_pantalla()

def mostrar_operacion(x):
    global texto_mostrar
    texto_mostrar += f"{x}"
    actualizar_pantalla()

def numero(num):
    mostrar_numero(num)

def operacion(op):
    mostrar_operacion(op)

def exponente():
    global texto_mostrar
    if not texto_mostrar.endswith("**"):
        texto_mostrar += "**"
    actualizar_pantalla()

def borrar_todo():
    global texto_mostrar
    texto_mostrar = "0"
    actualizar_pantalla()

def suprimir():
    global texto_mostrar
    if texto_mostrar == "0":
        pass
    elif len(texto_mostrar) == 1:
        texto_mostrar = "0"
    else:
        texto_mostrar = texto_mostrar[:-1]
    actualizar_pantalla()


ventana = tk.Tk()
ventana.title("Calculadora") # Nombre de la ventana
ventana.resizable(False, False) # Evitar que se cambie el tamaño de la ventana (Horizontal, Vertical)
ancho_pantalla = ventana.winfo_screenwidth() # Recoje valor de ancho de pantalla
alto_pantalla = ventana.winfo_screenheight() # Recoje valor de alto de pantalla
pos_x = (ancho_pantalla - 275) // 2 # Hace la operación para que quede centrado (ancho)
pos_y = (alto_pantalla - 400) // 2 # Hace la operación para que quede centrado (alto)
ventana.geometry(f"275x400+{pos_x}+{pos_y}") # Tamaño de la ventana (ancho x alto + posicionCentradaAncho + posicionCentradaAlto)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(5, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(11, weight=1)
color_de_fondo = "lightblue"
tamano_fuente = 10
ancho_botones = 5
altura_botones = 2
ventana.config(bg=color_de_fondo)

texto_por_pantalla = tk.Label(ventana, text=f"{texto_mostrar}", font=("Arial", tamano_fuente, "bold"), bg=color_de_fondo, anchor="e", width=30, height=altura_botones, bd=2, relief="sunken", background="white")
texto_por_pantalla.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

def actualizar_pantalla():
    global texto_mostrar
    if len(texto_mostrar) >= 34:
        texto_mostrar = texto_mostrar[:33]
        return
    else:
        texto_por_pantalla.config(text=texto_mostrar)

def coma():
    global texto_mostrar
    if texto_mostrar and texto_mostrar[-1] != ".":
        texto_mostrar += "."
    actualizar_pantalla()

def igual():
    global texto_mostrar, resultado
    try:
        resultado = eval(texto_mostrar)
        if len(str(resultado)) >= 34:
            texto_por_pantalla.config(text="Error, numero muy largo")
            texto_mostrar = ""
        else:
            texto_por_pantalla.config(text=resultado)
            texto_mostrar = str(resultado)
    except SyntaxError:
        texto_por_pantalla.config(text="Error")
        texto_mostrar = ""
    except ZeroDivisionError:
        texto_por_pantalla.config(text="No se puede divir entre 0")
        texto_mostrar = ""
    except ValueError:
        texto_por_pantalla.config(text="Error, numero muy largo")
        texto_mostrar = ""

boton = tk.Button(ventana, text=",", command=coma, width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=7, column=3, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="🟰", command=igual, width=ancho_botones, height=6, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=6, column=4, rowspan=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="➕", command=lambda: operacion("+"), width=ancho_botones, height=6, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=4, column=4, rowspan=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="➖", command=lambda: operacion("-"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=3, column=4, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="X", command=lambda: operacion("*"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=3, column=3, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="➗", command=lambda: operacion("/"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="x^y", command=exponente, width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="C", command=borrar_todo, width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="←", command=suprimir, width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="0", command=lambda: numero("0"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="1", command=lambda: numero("1"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="2", command=lambda: numero("2"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=6, column=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="3", command=lambda: numero("3"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=6, column=3, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="4", command=lambda: numero("4"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="5", command=lambda: numero("5"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=5, column=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="6", command=lambda: numero("6"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=5, column=3, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="7", command=lambda: numero("7"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="8", command=lambda: numero("8"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

boton = tk.Button(ventana, text="9", command=lambda: numero("9"), width=ancho_botones, height=altura_botones, font=("Arial", tamano_fuente, "bold"))
boton.grid(row=4, column=3, padx=5, pady=5, sticky="ew")

ventana.mainloop()