#Entrega Trabajo Intermedio
#Francisco Angelini
#26792677

from tkinter import Tk
from vistafran import VistaApp


class Miapp:
    def __init__(self, windows):
        # creo un atributo de instancia / el self hace referencia al objeto_miapp
        self.ventana = windows
        VistaApp(self.ventana)


if __name__ == "__main__":
    fran = Tk()
    # intancio (creo) la clase Miapp
    objeto_miapp = Miapp(fran)
    fran.mainloop()
