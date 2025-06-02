import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApp:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("cupcake.glade")  # archivo

        self.window = self.builder.get_object("cupcake")  # ID de la ventan
        

        self.window.connect("destroy", Gtk.main_quit)  # Para cerrar correctamente la ventana

        # Mostrar la ventana
        self.window.show_all()

if __name__ == "__main__":
    app = MyApp()
    Gtk.main()
