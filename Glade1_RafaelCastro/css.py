import sqlite3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

def aplicar_estilos(window, css_path="styles.css"):
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path(css_path)

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    
    print(f"Estilos cargados desde {css_path}")
    
def obtener_tema():
    """Recupera el tema guardado en la base de datos."""
    conn = sqlite3.connect("configuraciones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT tema FROM ajustes ORDER BY id DESC LIMIT 1")
    fila = cursor.fetchone()
    conn.close()
    return fila[0] if fila else None

def aplicar_tema(window):
    """Aplica el tema restaurado a la ventana."""
    tema_guardado = obtener_tema()
    if not tema_guardado:
        return

    style_context = window.get_style_context()
    style_context.remove_class("red-background")
    style_context.remove_class("blue-background")
    style_context.remove_class("green-background")
    style_context.remove_class("lightGray-background")

    if tema_guardado == "Rojo":
        style_context.add_class("red-background")
    elif tema_guardado == "Azul":
        style_context.add_class("blue-background")
    elif tema_guardado == "Verde":
        style_context.add_class("green-background")
    elif tema_guardado == "Gris":
        style_context.add_class("lightGray-background")

    print(f"Tema restaurado: {tema_guardado}")    
