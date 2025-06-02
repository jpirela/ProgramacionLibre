import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def abrir_glade(archivo_glade):
    builder = Gtk.Builder()
    builder.add_from_file(archivo_glade)

    ventana = builder.get_object("window1")
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()

    Gtk.main()

abrir_glade("menucomida.glade")