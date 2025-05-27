import sqlite3
from css import aplicar_estilos, aplicar_tema
# Conectar o crear la base de datos
conn = sqlite3.connect("configuraciones.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ajustes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    tema TEXT
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    cedula TEXT
)
""")
conn.commit()

cursor.execute("SELECT nombre, tema FROM ajustes ORDER BY id DESC LIMIT 1")
fila = cursor.fetchone()

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Ventana:
    def __init__(self):
            
        self.builder = Gtk.Builder()
        self.builder.add_from_file("ventana.glade")  # Cargar el archivo Glade
        self.window = self.builder.get_object("Window")  # ID de la ventana en Glade
        self.ventana_productos = self.builder.get_object("VentanaProductos")
        self.login_window = self.builder.get_object("LoginWindow")
        self.otra_ventana = self.builder.get_object("Proximamente")
        
        aplicar_estilos(self.window)
        aplicar_tema(self.window)
        
        self.combobox_tema = self.builder.get_object("combobox_tema")  # Obtener el widget
        self.combobox_tema.connect("changed", self.on_combobox_changed)  # Conectar evento

        
        self.Login_button = self.builder.get_object("boton")  
        self.Login_button.connect("clicked", self.Login_button_clicked)  # Conectar señal
        
        self.open_button = self.builder.get_object("open_window_button")  
        self.open_button.connect("clicked", self.on_open_window_clicked)
        
        self.save_button = self.builder.get_object("boton_guardar")
        self.save_button.connect("clicked", self.Save_Client)
        
        self.mostrar_button = self.builder.get_object("mostrar_usuario")
        self.mostrar_button.set_opacity(0.0)
        self.mostrar_button.connect("clicked", self.MostrarUsuario)
        
        self.Acceder = self.builder.get_object("Acceder")
        self.Acceder.connect("clicked", self.verificar_login)
        
        self.window.connect("destroy", self.on_destroy)  # Cerrar la app al salir
        self.ventana_productos.connect("delete-event", self.on_ventana_productos_close)
        self.login_window.connect("delete-event", self.on_login_window_close)
        self.otra_ventana.connect("delete-event", self.on_otra_ventana_close)
        self.window.show_all()
        
    def MostrarUsuario(self, widget):
        print("¡Botón clickeado!")
        if self.label.get_visible():
            self.label.set_visible(False)
        else:
            self.label.set_visible(True)
        
    def on_otra_ventana_close(self, widget, event):
        self.window.show_all()
        self.otra_ventana.hide()
        return True
        
    def Login_button_clicked(self, widget):
        print("¡Botón clickeado!")
        self.login_window.show_all()
        self.window.hide()
        self.ventana_productos.hide()
        
    def on_login_window_close(self, widget, event):
        self.window.show_all()
        self.login_window.hide()
        return True  # Indicar que el evento ha sido manejado
        
    def verificar_login(self, widget):    
        self.nombre = self.builder.get_object("LoginNombre").get_text()
        self.apellido = self.builder.get_object("LoginApellido").get_text()
        
        if not self.nombre or not self.apellido:
            self.mostrar_alerta("Por favor, ingresa tu nombre y apellido.")
            return
        
        # 🔍 Comprobar si el usuario existe en la base de datos
        cursor.execute("SELECT COUNT(*) FROM Cliente WHERE nombre = ? AND apellido = ?", (self.nombre, self.apellido))
        existe = cursor.fetchone()[0]

        if existe > 0:
            print(f"Usuario encontrado: {self.nombre} {self.apellido}. Abriendo nueva ventana...")
            self.cargar_nueva_ventana()
        else:
            self.mostrar_alerta("El usuario no existe en la base de datos.")    
    
    def cargar_nueva_ventana(self):
        self.login_window.hide()  # Ocultar ventana de login
        self.label = self.builder.get_object("LoginUser")
        self.label.set_text(f"Bienvenido, {self.nombre} {self.apellido}!")
        self.otra_ventana.show_all()  # Mostrar la nueva ventana
        self.label.set_visible(False)
        
    def mostrar_alerta(self, mensaje):
        dialog = Gtk.MessageDialog(
            parent=self.window,
            flags=Gtk.DialogFlags.MODAL,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK,
            text="Todos los campos son obligatorios."
        )
        dialog.run()
        dialog.destroy()    
        
    def Save_Client(self, widget):    
        nombre = self.builder.get_object("Nombre").get_text()
        apellido = self.builder.get_object("Apellido").get_text()
        cedula = self.builder.get_object("Cedula").get_text()
        
        if not nombre or not apellido or not cedula:
            self.mostrar_alerta("Todos los campos son obligatorios.")
            return  # Evita guardar datos incorrectos
        
        # 🛠 Comprobar si el usuario ya existe
        cursor.execute("SELECT COUNT(*) FROM Cliente WHERE nombre = ? AND apellido = ?", (nombre, apellido))
        existe = cursor.fetchone()[0]

        if existe > 0:
            self.mostrar_alerta("Este usuario ya está registrado.")
            return
        
        # 📝 Guardar en la base de datos si no existe
        cursor.execute("INSERT INTO Cliente (nombre, apellido, cedula) VALUES (?, ?, ?)", (nombre, apellido, cedula))
        conn.commit()

        print(f"Cliente guardado: {nombre} {apellido}, Cédula: {cedula}")
    
    def on_open_window_clicked(self, widget):
        self.ventana_productos.show_all()  # Mostrar la segunda ventana  
        
    def on_destroy(self, widget):
        conn.commit()  # Guarda cualquier cambio pendiente
        conn.close()  # Cierra correctamente la conexión
        Gtk.main_quit() 
        
    def on_ventana_productos_close(self, widget, event):
        self.ventana_productos.hide()  # Ocultar en lugar de destruir
        return True  # Prevenir el cierre real   
        
    def on_combobox_changed(self, widget):
        print(f"Nuevo tema seleccionado: {widget.get_active_text()}")
        tema = widget.get_active_text()  # Obtener la opción seleccionada
    
        style_context = self.window.get_style_context()

        # Remover clases anteriores
        style_context.remove_class("red-background")
        style_context.remove_class("blue-background")
        style_context.remove_class("green-background")
        style_context.remove_class("lightGray-background")

        # Aplicar la nueva clase según el tema seleccionado
        if tema == "Rojo":
            style_context.add_class("red-background")
        elif tema == "Azul":
            style_context.add_class("blue-background")
        elif tema == "Verde":
            style_context.add_class("green-background")
        elif tema == "Gris":
            style_context.add_class("lightGray-background")
            
            # 🛠 Guardar el tema seleccionado en SQLite
        cursor.execute("SELECT COUNT(*) FROM ajustes")
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.execute("INSERT INTO ajustes (tema) VALUES (?)", (tema,))
        else:
            cursor.execute("UPDATE ajustes SET tema = ? WHERE id = (SELECT MAX(id) FROM ajustes)", (tema,))
        conn.commit()
        print(f"Tema guardado en SQLite: {tema}")
            

app = Ventana()
Gtk.main()
conn.close()
