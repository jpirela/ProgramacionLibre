import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MiVentana:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Proyecto_1_AndresPetit.glade")
        self.ventana = self.builder.get_object("nombre_de_la_ventana")
        self.ventana.connect("destroy", Gtk.main_quit)
        self.ventana.show_all()

if __name__ == "__main__":
    app = MiVentana()
    Gtk.main()