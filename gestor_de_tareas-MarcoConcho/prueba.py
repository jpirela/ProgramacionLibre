import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApp:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("tareas2.glade")  # archivo

        self.window = self.builder.get_object("gestor de tareas")  # ID de la ventan
        #intento de dar funcionalidad a los combobox mas adelante lo hare 
        """combo = self.builder.get_object("combobox_prioridad")  # Asegúrate del ID correcto
        combo = Gtk.ComboBoxText()  # Convertirlo en GtkComboBoxText
        combo.append_text("poco urgente")
        combo.append_text("urgente")
        combo.append_text("moderadamente urgente")

        combo2 = self.builder.get_object("combobox_estado")  # Asegúrate del ID correcto
        combo2 = Gtk.ComboBoxText()  # Convertirlo en GtkComboBoxText
        combo2.append_text("pendiente")
        combo2.append_text("terminada")
        combo2.append_text("pausada")"""

        self.window.connect("destroy", Gtk.main_quit)  # Para cerrar correctamente la ventana

        # Mostrar la ventana
        self.window.show_all()

if __name__ == "__main__":
    app = MyApp()
    Gtk.main()
