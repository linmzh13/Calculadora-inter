import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("290x350")
        self.ventana.resizable(False, False)

        self.pantalla = tk.Entry(
            ventana,
            font=("Arial", 18),
            justify="right"
        )
        self.pantalla.grid(row=0, column=0, columnspan=4,
                           padx=10, pady=15, ipady=8)

        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("C", 4, 0), ("0", 4, 1), (".", 4, 2),
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3),
            ("/", 4, 3)
        ]

        for texto, fila, columna in botones:
            if texto == "C":
                accion = self.borrar
            else:
                accion = lambda valor=texto: self.escribir(valor)

            boton = tk.Button(
                ventana,
                text=texto,
                font=("Arial", 11),
                width=5,
                height=2,
                command=accion
            )
            boton.grid(row=fila, column=columna, padx=3, pady=3)

        boton_igual = tk.Button(
            ventana,
            text="=",
            font=("Arial", 11),
            width=24,
            height=2,
            command=self.calcular
        )
        boton_igual.grid(row=5, column=0, columnspan=4,
                         padx=5, pady=5)

    def escribir(self, numero):
        self.pantalla.insert(tk.END, numero)

    def borrar(self):
        self.pantalla.delete(0, tk.END)

    def calcular(self):
        try:
            operacion = self.pantalla.get()
            resultado = eval(operacion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, str(resultado))

        except Exception:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")


ventana = tk.Tk()
calculadora = Calculadora(ventana)
ventana.mainloop()