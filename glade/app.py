import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Mi Aplicación con Glade")

        # Cargar la interfaz desde el archivo Glade
        builder = Gtk.Builder()
        builder.add_from_file("ejercicio.glade")

        # Obtener el objeto de la ventana principal
        self.window = builder.get_object("main")
        self.window.connect("destroy", Gtk.main_quit)

        # Mostrar la ventana
        self.window.show_all()

if __name__ == "__main__":
    app = MyApp()
    Gtk.main()
    
