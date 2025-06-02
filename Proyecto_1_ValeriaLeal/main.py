import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentanaApp:
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Proyecto_1_ValeriaLeal/CalendariodeFormula1.glade")

        
        self.window = self.builder.get_object("main_ventana") 
        if not self.window: 
            self.window = self.builder.get_object("ventanaPrincipal") 

        
        self.window.set_default_size(800, 650)

       
        self.window.set_resizable(False)

       
        self.window.connect("destroy", Gtk.main_quit)

    def run(self):
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    app = MiVentanaApp()
    app.run()