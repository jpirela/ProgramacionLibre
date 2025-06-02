import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CalculadoraGTK:
    def __init__(self):
        # Cargar interfaz desde Glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file("calculadora.glade")
        
        # Configurar widgets
        self.entrada = self.builder.get_object("entrada_resultado")
        
        # Conectar señales
        self.builder.connect_signals({
            "on_boton_clicked": self.on_boton_clicked,
            "on_igual_clicked": self.on_igual_clicked,
            "on_limpiar_clicked": self.on_limpiar_clicked,
            "on_destroy": Gtk.main_quit
        })
        
        # Mostrar ventana
        self.ventana = self.builder.get_object("ventana_principal")
        self.ventana.show_all()

    def on_boton_clicked(self, widget):
        """Maneja clics en botones numéricos/operadores"""
        texto_actual = self.entrada.get_text()
        nuevo_texto = texto_actual + widget.get_label() if texto_actual != "0" else widget.get_label()
        self.entrada.set_text(nuevo_texto)

    def on_igual_clicked(self, widget):
        """Calcula el resultado"""
        try:
            resultado = str(eval(self.entrada.get_text()))
            self.entrada.set_text(resultado)
        except:
            self.entrada.set_text("Error")

    def on_limpiar_clicked(self, widget):
        """Limpia la pantalla"""
        self.entrada.set_text("0")

if __name__ == "__main__":
    app = CalculadoraGTK()
    Gtk.main()