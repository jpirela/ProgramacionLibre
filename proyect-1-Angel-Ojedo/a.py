import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SimpleDesktopApp:
    def __init__(self, glade_path):
        self.builder = Gtk.Builder()
        try:
            self.builder.add_from_file(glade_path)
        except Exception as e:
            print(f"Error al cargar el archivo Glade: {e}")
            exit(1)
        
        # Se obtiene la referencia a la ventana principal definida en el archivo Glade.
        self.window = self.builder.get_object("main_window")
        if self.window is None:
            print("No se encontró el objeto 'main_window' en el archivo Glade.")
            exit(1)
        
        # Conecta la señal 'destroy' para que la aplicación se cierre correctamente.
        self.window.connect("destroy", self.on_destroy)

    def on_destroy(self, widget):
        """Finaliza la aplicación cuando se cierra la ventana."""
        Gtk.main_quit()

    def run(self):
        """Muestra la ventana y comienza el bucle principal de GTK."""
        self.window.show_all()
        Gtk.main()


if __name__ == "__main__":
    app = SimpleDesktopApp("Unsaved 1.glade")
    app.run()