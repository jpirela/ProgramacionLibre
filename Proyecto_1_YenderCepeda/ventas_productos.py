import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SistemaVentas:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ventas_productos.glade")
        self.window = builder.get_object("main_window")
        self.window.connect("destroy", Gtk.main_quit)

        self.entry_nombre = builder.get_object("entry_nombre")
        self.entry_cantidad = builder.get_object("entry_cantidad")
        self.entry_precio = builder.get_object("entry_precio")

        self.button_agregar = builder.get_object("button_agregar")
        self.button_eliminar = builder.get_object("button_eliminar")

        self.button_agregar.connect("clicked", self.agregar_producto)
        self.button_eliminar.connect("clicked", self.eliminar_producto)

        self.treeview = builder.get_object("treeview_productos")
        self.modelo = Gtk.ListStore(str, int, float)
        self.treeview.set_model(self.modelo)

        renderer_nombre = Gtk.CellRendererText()
        columna_nombre = Gtk.TreeViewColumn("Nombre del producto", renderer_nombre, text=0)
        self.treeview.append_column(columna_nombre)

        renderer_cantidad = Gtk.CellRendererText()
        columna_cantidad = Gtk.TreeViewColumn("Cantidad", renderer_cantidad, text=1)
        self.treeview.append_column(columna_cantidad)

        renderer_precio = Gtk.CellRendererText()
        columna_precio = Gtk.TreeViewColumn("Precio", renderer_precio)
        columna_precio.set_cell_data_func(renderer_precio, self.formatear_precio)
        self.treeview.append_column(columna_precio)

        self.window.show_all()

    def formatear_precio(self, column, cell, model, iter, data=None):
        precio = model.get_value(iter, 2)
        cell.set_property("text", f"${precio:,.2f}")

    def agregar_producto(self, button):
        nombre = self.entry_nombre.get_text().strip()
        cantidad_texto = self.entry_cantidad.get_text().strip()
        precio_texto = self.entry_precio.get_text().strip()

        if not nombre or not cantidad_texto or not precio_texto:
            self.mostrar_error("Por favor completa todos los campos.")
            return
        try:
            cantidad = int(cantidad_texto)
            precio = float(precio_texto)
        except ValueError:
            self.mostrar_error("Cantidad debe ser un número entero y Precio un número válido.")
            return

        self.modelo.append([nombre, cantidad, precio])
        self.entry_nombre.set_text("")
        self.entry_cantidad.set_text("")
        self.entry_precio.set_text("")

    def eliminar_producto(self, button):
        selection = self.treeview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter is None:
            self.mostrar_error("Selecciona un producto para eliminar.")
            return
        model.remove(treeiter)

    def mostrar_error(self, mensaje):
        dialog = Gtk.MessageDialog(
            transient_for=self.window,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=mensaje,
        )
        dialog.run()
        dialog.destroy()

if __name__ == "__main__":
    app = SistemaVentas()
    Gtk.main()
