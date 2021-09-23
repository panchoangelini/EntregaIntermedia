from tkinter import messagebox
from tkinter.constants import END, EW
import mysql.connector
import re
from tkinter import Label

class Conexion:
    """Se crea la conexion inicial a la base de datos"""
    def __init__(self,):
        """Se crea el constructor de la clase"""
        print("Conexion de Arranque")
    
    def creabase(self,):
        """Se crea la base de datos en caso de que no exista"""
        try:
            self.franangelini = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
            )
            self.micursor = self.franangelini.cursor()
            self.micursor.execute("CREATE DATABASE IF NOT EXISTS basefran")
            self.franangelini1 = mysql.connector.connect(
                host="localhost", user="root", passwd="", database="basefran"
            )
            self.micursor1 = self.franangelini1.cursor()
            self.micursor1.execute(
                "CREATE TABLE IF NOT EXISTS producto(idproducto int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, producto VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, talle VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,descripcion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,marca VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)"
            )
            messagebox.showinfo(
                message="La Tabla ya ha sido creada", title="Tabla")
            print("La Tabla ya ha sido creada")
        except:
            messagebox.showinfo(
                message="La Base de Datos ya ha sido creada", title="Base"
            )
            print("La base de datos ya Existe")
print("---------- Informacion Sobre La Clase Conexion---------")
print(Conexion.__doc__)
print("---------- Informacion Sobre El Metodo Init---------")
print(Conexion.__init__.__doc__)
print("---------- Informacion Sobre El Metodo Crearbase---------")
print(Conexion.creabase.__doc__)

class Miconexion:
    """Se crea una conexion permanente para distintos metodos"""
    def __init__(self,):
        """Se crea el constructor de la clase"""
        print("Conexion")

    def mi_conexion(self,):
        """Conexion directa a Mysql as la base de nombres basefran"""
        franangelini = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="basefran"
        )
        return franangelini
print("---------- Informacion Sobre La Clase MiConexion---------")
print(Miconexion.__doc__)
print("---------- Informacion Sobre El Metodo Init---------")
print(Miconexion.__init__.__doc__)
print("---------- Informacion Sobre El Metodo mi_conexion---------")
print(Miconexion.mi_conexion.__doc__)

class MostrarTreeView:
    """Se desarrolla el metodo para mostrar los datos de basefran en el treeview"""
    def __init__(self,):
        """Se crea el constructor de la clase"""
        print("Mostrar Treeview")

    def mostrartree(self,tree):
        """Conexion a basefran"""
        franangelini = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="basefran"
        )
        micursor = franangelini.cursor()
        """Se crea la variable para seleccionar datos de basefran"""
        sql = "SELECT * FROM producto"
        micursor.execute(sql)
        resultado = micursor.fetchall()
        """Se genera el ingreso de los datos al treeview y se ubica en el grid"""
        for x in resultado:
            print(x)
            tree.insert("", "end", text=x[0], values=(x))
        tree.grid(row=6, column=0, columnspan=2, sticky=EW)
print("---------- Informacion Sobre La Clase MostrarTreevView---------")
print(MostrarTreeView.__doc__)
print("---------- Informacion Sobre El Metodo Init---------")
print(MostrarTreeView.__init__.__doc__)
print("---------- Informacion Sobre El Metodo mostrartree---------")
print(MostrarTreeView.mostrartree.__doc__)
    
class Abmc:
    """Se crea la Clase Abmc para realizar las acciones de alta, baja, modificacion y consulta"""
    def __init__(self,):
        """Se crea el constructor de la clase"""
        print("Abmc")

    def actualizar_treeview(self, producto,talle,descripcion,marca,tree):
        """Se crea el metodo actualizar para utilizar en cada metodo del abmc
           Se crea una excepcion en caso de no contar con una conexion a la base de datos
           Se crea la conexion a la base de datos
           Se limpian los campos entry
           Se actualiza el treeview
           Se crea la Excepcion en caso de que no exista la conexion a la base de datos
           """
        try:
            """Se crea la conexion a la base de datos"""
            franangelini = Miconexion.mi_conexion(self,)
            micursor = franangelini.cursor()
            sql = "SELECT * FROM producto  ORDER BY idproducto DESC"
            micursor.execute(sql)
            cargatree = micursor.fetchall()
            """Se limpian los campos entry"""
            producto.delete(0, END)
            talle.delete(0, END)
            descripcion.delete(0, END)
            marca.delete(0, END)
            """Se actualiza el treeview"""
            tree.delete(*tree.get_children())
            for x in cargatree:
                tree.insert("", 0, text="", values=x)
        except:
            """Excepcion en caso de que no exista la conexion a la base de datos"""
            messagebox.showerror(
                message="Error al conectar con base de datos", title="Pal Ocote"
            )

    def alta(self,producto, talle, descripcion,marca,tree,ventana):
        """Se crea el metodo alta de datos"""
        print("Alta")
        print("Nueva Alta de Datos")
        cadena = descripcion.get()
        patron = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"
        if re.match(patron, cadena):
            Label(
                ventana,
                text="Alcoyana Alcoyana Usted Ingreso..." + descripcion.get(),
                font=("Calibri", 16),
            ).place(x=250, y=30)
            print("Validado")
            franangelini = Miconexion.mi_conexion(self,)
            micursor = franangelini.cursor()
            sql = "INSERT INTO producto (producto, talle, descripcion, marca) VALUES (%s,%s,%s,%s)"
            datos = (producto.get(), talle.get(), descripcion.get(), marca.get())
            micursor.execute(sql, datos)
            tree.insert("", 0, text="", values=())
            franangelini.commit()
            self.actualizar_treeview(producto,talle,descripcion,marca,tree)

        else:
            Label(
                ventana,
                text="Usted Ingreso: "
                + descripcion.get()
                + ", Por favor ingrese una descripcion sin numeros",
                font=("Calibri", 16),
            ).place(x=40, y=20)
            print("NO validado")
            messagebox.showinfo(
                message="Usted Ingreso un dato incorrecto, por favor ingrese una descripcion sin numeros",
                title="Error de Carga",)

    def seleccionar(self,producto, talle, descripcion,marca,tree,temp_label):
        """Se crea el metodo para seleccion de datos"""
        selec = tree.focus()
        selecfran = tree.item(selec)
        print(selecfran["text"])
        selecfran2 = selecfran["values"]
        print(selecfran2)
        temp_label.config(text=selecfran2)

        producto.insert(0, selecfran2[1])
        talle.insert(0, selecfran2[2])
        descripcion.insert(0, selecfran2[3])
        marca.insert(0, selecfran2[4])

        franangelini = Miconexion.mi_conexion(self,)
        micursor = franangelini.cursor()
        sql = "SELECT idproducto = %s, producto = %s, talle = %s, descripcion = %s, marca = %s FROM producto"
        micursor.execute(sql, selecfran2)
        seleccionfran = micursor.fetchall()
        print(seleccionfran)
        franangelini.commit()

    def actualizar(self,producto, talle, descripcion,marca,tree):
        """Se crea el metodo para actualizar datos"""
        actualizar1 = tree.focus()
        actualizar2 = tree.item(actualizar1)
        actualizar3 = actualizar2["values"]
        actualizar5 = actualizar2["text"]
        print(actualizar5)
        franangelini = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="basefran"
        )
        micursor = franangelini.cursor()
        sql = "UPDATE producto SET producto=%s, talle=%s, descripcion=%s, marca=%s WHERE idproducto=%s"
        actual = (producto.get(), talle.get(), descripcion.get(), marca.get(), actualizar5)
        micursor.execute(sql, actual)
        producto.delete(0, END)
        talle.delete(0, END)
        descripcion.delete(0, END)
        marca.delete(0, END)
        franangelini.commit()
        self.actualizar_treeview(producto,talle,descripcion,marca,tree)
    
    def borrar(self,tree,producto,talle,descripcion,marca):
        """Se crea el metodo para borrar datos"""
        id = tree.focus()
        print(id)
        borrafran = tree.item(id)
        print(tree.item(id))
        print(borrafran["text"])
        borrafran2 = borrafran["text"]
        print(borrafran2)

        franangelini = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="basefran"
        )
        micursor = franangelini.cursor()
        sql = "DELETE FROM producto WHERE idproducto = %s"
        datodelete = (borrafran2,)
        micursor.execute(sql, datodelete)
        franangelini.commit()
        tree.delete(id)
        print(micursor.rowcount, "Registro borrado")
        producto.delete(0, END)
        talle.delete(0, END)
        descripcion.delete(0, END)
        marca.delete(0, END)

print("---------- Informacion Sobre La Clase Abmc---------")
print(Abmc.__doc__)
print("---------- Informacion Sobre El Metodo Init---------")
print(Abmc.__init__.__doc__)
print("---------- Informacion Sobre El Metodo actualizar_treeview---------")
print(Abmc.actualizar_treeview.__doc__)
print("---------- Informacion Sobre El Metodo alta---------")
print(Abmc.alta.__doc__)
print("---------- Informacion Sobre El Metodo seleccionar---------")
print(Abmc.seleccionar.__doc__)
print("---------- Informacion Sobre El Metodo actualizar---------")
print(Abmc.actualizar.__doc__)
print("---------- Informacion Sobre El Metodo borrar---------")
print(Abmc.borrar.__doc__)

class Varios:
    """Se crea la Clase Varios para realizar las acciones complementarios al formulario de carga"""
    def __init__(self,):
        """Se crea el constructor de la clase"""
        print("Varios")
    
    def color(self,random,color):
        """Se crea el metodo color para cambiar aleatoriamente el color de fondo del formulario"""
        self.fran.config(background=random.choice(color))
        color

    def limpiar(self,producto, talle, descripcion,marca):
        """Se crea el metodo limpiar para borar los datos de los entrys en el formulario de carga"""
        producto.delete(0, END)
        talle.delete(0, END)
        descripcion.delete(0, END)
        marca.delete(0, END)
print("---------- Informacion Sobre La Clase Varios---------")
print(Varios.__doc__)
print("---------- Informacion Sobre El Metodo Init---------")
print(Varios.__init__.__doc__)
print("---------- Informacion Sobre El Metodo color---------")
print(Varios.color.__doc__)       
print("---------- Informacion Sobre El Metodo limpiar---------")
print(Varios.limpiar.__doc__)   
  