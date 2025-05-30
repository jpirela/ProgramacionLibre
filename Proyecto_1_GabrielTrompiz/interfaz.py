import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class MyApp:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("C:\\Users\\Guardia AIT\\Desktop\\interfaz de usuario\\interfaz de usuario.glade")
        # Usa el ID correcto de la ventana principal
        self.window = self.builder.get_object("window")

        if self.window is None:
            print("Error: No se pudo encontrar la ventana principal en Glade. Verifica el ID.")
            return

        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

if __name__ == "__main__":
    app = MyApp()
    Gtk.main()