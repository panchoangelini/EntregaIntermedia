import random
from tkinter import Frame
from tkinter import messagebox
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter.constants import ANCHOR, CENTER, E, END, EW, RAISED, W
from tkinter import StringVar
from tkinter import ttk
from modelofran import Abmc, Conexion, MostrarTreeView, Varios
from parametrosfran import color


class VistaApp:
    """Se crean las variables y metodos necesarios para la vista del formulario"""
    def __init__(self, windows):
        """ #Se crea el constructor inicial
            ################################################################
            #Se crean las variables principales para la construccion del formulario de carga de datos
            #Se crean los objetos POO para conexion
            ################################################################
            #Se crean etiquetas del titulo del formulario
            ################################################################
            #Se crean etiquetas del formulario
            #Se crea el frame para avisos sobre ingreso de datos
            ################################################################
            #Se definen variables
            ################################################################
            #Se define el lugar donde se ubicaran los labels en el formulario
            #Se crean variables para toma de datos
            ################################################################
            #Se Crean los Botones
            #Se crea el Boton de cambio de color del fondo
            #Se crea el Boton de limpiar labels del formulario
            #Se crea el Boton para Agregar Registro a formulario y base de datos
            #Se crea el Boton para Seleccionar Registro a formulario y base de datos
            #Se crea el Boton de Guardado de Productos por consola
            #Se crea el Boton para Borrar Registro a formulario y base de datos
            #Se crea el Boton para Actualizar Registro a formulario y base de datos
            #Se crea el boton Salir del Formulario
            ################################################################
            #Se crea el Treeview
            ################################################################
            #Se crea el label para confirmar la seleccion de una fila
            ################################################################
            #Se cran los metodos para trabajar con los objetos POO
            ################################################################
            #Metodo de conexion de arranque para creacion de base de datos y tabla en el caso que no se encuentre creada
        """
        
        ################################################################
        #Se crean las variables principales para la construccion del formulario de carga de datos
        #Se crean los objetos POO para conexion
        ################################################################
        self.fran = windows
        self.fran.title("Desafio App")
        self.fran.geometry("725x725")
        self.fran.anchor("n")
        self.tree = ttk.Treeview(self.fran)
        self.objeto_conexion_arranque = Conexion.creabase(self,)
        self.objeto_mostrartreeview = MostrarTreeView.mostrartree(self,self.tree)
        self.objeto_Ambc = Abmc()
        self.objeto_varios = Varios()

        ################################################################
        #Se crean las etiquetas del titulo del formulario
        ################################################################
        self.titulo = Label(
            text="Ingrese Datos del Producto", bg="deep sky blue", height=1, width=50
        )
        self.titulo.grid(row=0, column=0, padx=5, pady=5,
                         columnspan=2, sticky=W + E)

        """Se crean las etiquetas del formulario"""
        self.labelproducto = Label(text="Producto", fg="Black", bg="Orange").grid(
            row=1, column=0, padx=5, pady=5, sticky=W
        )
        self.labeltalle = Label(text="Talle", fg="Black", bg="Orange").grid(
            row=2, column=0, padx=5, pady=5, sticky=W
        )
        self.labeldescripcion = Label(text="Descripcion", fg="Black", bg="Orange").grid(
            row=3, column=0, padx=5, pady=5, sticky=W
        )
        self.labelmarca = Label(text="Marca", fg="Black", bg="Orange").grid(
            row=4, column=0, padx=5, pady=5, sticky=W
        )
        """Se crea el frame para avisos sobre ingreso de datos"""
        self.ventana = Frame(bg="cyan", height=80,
                             borderwidth=2, relief=RAISED)
        self.ventana.grid(row=5, column=0, padx=5, pady=5,
                          columnspan=2, sticky=W + E)

        ################################################################
        #Se definen las variables
        ################################################################
        self.producto = StringVar()
        self.talle = StringVar()
        self.descripcion = StringVar()
        self.marca = StringVar()

        self.producto = ttk.Combobox(
            self.fran,
            values=["Remera", "Pantalon", "Buzo", "Medias", "Calzas", "Short"],
            width=20,
        )
        self.talle = ttk.Combobox(
            self.fran, values=["S", "M", "L", "XL", "XXL"], width=20
        )
        self.descripcion = Entry(self.fran, width=20)
        self.marca = ttk.Combobox(
            self.fran,
            values=["Nike", "Adidas", "Puma", "Under Armor", "Reebok"],
            width=20,
        )
        #Se define el lugar donde se ubicaran los labels en el formulario
        self.producto.grid(row=1, column=1, padx=5, pady=6, sticky=W)
        self.talle.grid(row=2, column=1, padx=5, pady=6, sticky=W)
        self.descripcion.grid(row=3, column=1, padx=5, pady=6, sticky=W)
        self.marca.grid(row=4, column=1, padx=5, pady=6, sticky=W)
        
        #Se crean variables para toma de datos
        self.datos1 = self.producto.get()
        self.datos2 = self.talle.get()
        self.datos3 = self.descripcion.get()
        self.datos4 = self.marca.get()
        self.datos = (self.datos1, self.datos2, self.datos3, self.datos4)

        ################################################################
        #Se Crean los Botones
        ################################################################

        #boton de cambio de color del fondo
        self.cambiar_color = Button(
            self.fran,
            command=lambda: self.colorfran(),
            text="Cambiar Color Fondo",
            padx=30,
            pady=1,
            width=12,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 10, "bold"),
        )
        self.cambiar_color.grid()
        self.cambiar_color.place(x=520, y=45)

        #Se crea el boton de limpiar labels del formulario"""
        self.limpiarregistro = Button(
            self.fran,
            command=lambda: self.limpiarfran(),
            text="limpiar",
            padx=30,
            pady=1,
            width=12,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 10, "bold"),
        )
        self.limpiarregistro.grid()
        self.limpiarregistro.place(x=520, y=95)

        #Se crea el Boton para Agregar Registro a formulario y base de datos"""
        self.agregar = Button(
            self.fran,
            command=lambda: self.altafran(),
            text="Agregar Registro",
            padx=30,
            pady=2,
            width=15,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 12, "bold"),
        )
        self.agregar.grid()
        self.agregar.place(x=75, y=500)

        #Se crea el Boton para Seleccionar Registro a formulario y base de datos"""
        self.seleccionar = Button(
            self.fran,
            command= lambda: self.seleccionarfran(),
            text="Seleccionar Registro",
            padx=30,
            pady=2,
            width=15,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 12, "bold"),
        )
        self.seleccionar.grid()
        self.seleccionar.place(x=75, y=575)

        #Creo Boton de Guardado de Productos por consola"""
        self.guardar = Button(
            self.fran,
            text="Guardar en Consola",
            padx=30,
            pady=2,
            width=15,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 12, "bold"),
        )
        self.guardar.grid()
        self.guardar.place(x=425, y=500)

        #Se crea el Boton para Borrar Registro a formulario y base de datos"""
        self.borraras = Button(
            self.fran,
            command= lambda: self.borrarfran(),
            text="Borrar Registro",
            padx=30,
            pady=2,
            width=15,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 12, "bold"),
        )
        self.borraras.grid()
        self.borraras.place(x=425, y=575)

        #Se crea el Boton para Actualizar Registro a formulario y base de datos"""
        self.actualizar = Button(
            self.fran,
            command= lambda: self.actualizarfran(),
            text="Actualizar Registro",
            padx=30,
            pady=2,
            width=15,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 12, "bold"),
        )
        self.actualizar.grid()
        self.actualizar.place(x=75, y=650)

        #Se crea el boton Salir del Formulario"""
        self.salir = Button(
            self.fran,
            command=lambda: self.salirfran(),
            text="Salir",
            padx=30,
            pady=2,
            width=15,
            height=2,
            activebackground="green",
            activeforeground="orange",
            background="black",
            foreground="orange",
            anchor=CENTER,
            font=("courier", 12, "bold"),
        )
        self.salir.grid()
        self.salir.place(x=425, y=650)

        ################################################################
        #Se crea el Treeview"""
        ################################################################
        self.tree["columns"] = ("uno", "dos", "tres", "cuatro", "cinco")
        self.tree.grid(row=7, column=0, columnspan=2)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("uno", text="idproducto", anchor=CENTER)
        self.tree.heading("dos", text="producto", anchor=CENTER)
        self.tree.heading("tres", text="talle", anchor=CENTER)
        self.tree.heading("cuatro", text="descripcion", anchor=CENTER)
        self.tree.heading("cinco", text="marca", anchor=CENTER)
        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("uno", width=130)
        self.tree.column("dos", width=130)
        self.tree.column("tres", width=130)
        self.tree.column("cuatro", width=130)
        self.tree.column("cinco", width=130)
        
        ################################################################
        #Se crea el label para confirmar la seleccion de una fila"""
        ################################################################
        self.temp_label = Label(
            self.fran,
            text="",
        )
        self.temp_label.grid()

    ################################################################"""
    #Se cran los metodos para trabajar con los objetos POO"""
    ################################################################"""
    #Metodo de conexion de arranque para creacion de base de datos y tabla en el caso que no se encuentre creada"""
    def conexion_vista(self,):
        """Metodo para mostrar el treeview en el formulario"""
        self.objeto_conexion_arranque.__init__(self,)
    def mostrartreeview(self,):
        """Metodo para mostrar el Treeview en el formulario"""
        self.objeto_mostrartreeview(self.tree)
        
    def altafran(self,):
        """Metodo para dar de alta un registro"""
        self.objeto_Ambc.alta(self.producto,self.talle,self.descripcion,self.marca,self.tree,self.ventana)
        
    def actualizartreeview(self,):
        """Metodo para actualizar los datos del treeview luego de una accion"""
        self.objeto_Ambc.actualizar_treeview(self, self.producto,self.talle,self.descripcion,self.marca,self.tree)
        
    def seleccionarfran(self,):
        """Metodo para seleccioinar un registro"""
        self.objeto_Ambc.seleccionar(self.producto,self.talle,self.descripcion,self.marca,self.tree,self.temp_label)
        
    def actualizarfran(self,):
        """Metodo para actualizar un registro"""
        self.objeto_Ambc.actualizar(self.producto,self.talle,self.descripcion,self.marca,self.tree)
        
    def borrarfran(self,):
        """Metodo para borrar un registro"""
        self.objeto_Ambc.borrar(self.tree,self.producto,self.talle,self.descripcion,self.marca)
        
    def salirfran(self,):
        """Metodo para salir del formulario"""
        self.fran.destroy()
        
    def colorfran(self,):
        """Metodo para cambiar color del formulario"""
        self.objeto_varios.color(self.random,self.color)
        
    def limpiarfran(self,):
        """Metodo para limpiar entrys"""
        self.objeto_varios.limpiar(self.producto,self.talle,self.descripcion,self.marca,self.tree)

print("---------- Informacion Sobre La Clase VistaApp---------")
print(VistaApp.__doc__)
print("---------- IInformacion Sobre El Metodo Init---------")
print(VistaApp.__init__.__doc__)
print("---------- Informacion Sobre El Metodo conexion_vista---------")
print(VistaApp.conexion_vista.__doc__)
print("---------- Informacion Sobre El Metodo mostrartreeview---------")
print(VistaApp.mostrartreeview.__doc__)  
print("---------- Informacion Sobre El Metodo altafran---------")
print(VistaApp.altafran.__doc__)      
print("---------- Informacion Sobre El Metodo actualizartreeview---------")
print(VistaApp.actualizartreeview.__doc__)
print("---------- Informacion Sobre El Metodo seleccionarfran---------")
print(VistaApp.seleccionarfran.__doc__)
print("---------- Informacion Sobre El Metodo actualizarfran---------")
print(VistaApp.actualizarfran.__doc__)
print("---------- Informacion Sobre El Metodo borrarfran---------")
print(VistaApp.borrarfran.__doc__)
print("---------- Informacion Sobre El Metodo salirfran---------")
print(VistaApp.salirfran.__doc__)
print("---------- Informacion Sobre El Metodo colorfran---------")
print(VistaApp.colorfran.__doc__)
print("---------- Informacion Sobre El Metodo limpiarfran---------")
print(VistaApp.limpiarfran.__doc__)