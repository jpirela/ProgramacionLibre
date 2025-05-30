import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

GLADE_FILE = "Proyecto_1_Gabriel_Cabrera.glade"

def on_window_destroy(window, data=None):
    Gtk.main_quit()

def cargar_glade():
    builder = Gtk.Builder()
    builder.add_from_file(GLADE_FILE)

    window = builder.get_object("main_window")
    window.connect("destroy", on_window_destroy)

    window.show_all()

if __name__ == "__main__":
    cargar_glade()
    Gtk.main()