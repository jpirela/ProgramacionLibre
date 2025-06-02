import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VentaVehiculos:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ventavehiculos.glade")
        self.window = builder.get_object("main_window")
        self.window.connect("destroy", Gtk.main_quit)
        self.entry_marca = builder.get_object("entry_marca")
        self.entry_modelo = builder.get_object("entry_modelo")
        self.entry_ano = builder.get_object("entry_ano")
        self.entry_precio = builder.get_object("entry_precio")
        self.button_agregar = builder.get_object("button_agregar")
        self.button_agregar.connect("clicked", self.agregar_vehiculo)
        self.button_eliminar = builder.get_object("button_eliminar")
        self.button_eliminar.connect("clicked", self.eliminar_vehiculo)
        self.treeview = builder.get_object("treeview_vehicles")
        self.modelo = Gtk.ListStore(str, str, int, float)
        self.treeview.set_model(self.modelo)
        renderer_marca = Gtk.CellRendererText()
        columna_marca = Gtk.TreeViewColumn("Marca", renderer_marca, text=0)
        self.treeview.append_column(columna_marca)
        renderer_modelo = Gtk.CellRendererText()
        columna_modelo = Gtk.TreeViewColumn("Modelo", renderer_modelo, text=1)
        self.treeview.append_column(columna_modelo)
        renderer_ano = Gtk.CellRendererText()
        columna_ano = Gtk.TreeViewColumn("Año", renderer_ano, text=2)
        self.treeview.append_column(columna_ano)
        renderer_precio = Gtk.CellRendererText()
        columna_precio = Gtk.TreeViewColumn("Precio", renderer_precio)
        columna_precio.set_cell_data_func(renderer_precio, self.formatear_precio)
        self.treeview.append_column(columna_precio)
        self.window.show_all()

    def formatear_precio(self, column, cell, model, iter, data=None):
        precio = model.get_value(iter, 3)
        cell.set_property("text", f"${precio:,.2f}")

    def agregar_vehiculo(self, button):
        marca = self.entry_marca.get_text().strip()
        modelo = self.entry_modelo.get_text().strip()
        ano_texto = self.entry_ano.get_text().strip()
        precio_texto = self.entry_precio.get_text().strip()
        if not marca or not modelo or not ano_texto or not precio_texto:
            self.mostrar_error("Por favor, completa todos los campos.")
            return
        try:
            ano = int(ano_texto)
            precio = float(precio_texto)
        except ValueError:
            self.mostrar_error("Año debe ser un número entero y Precio un número válido.")
            return
        self.modelo.append([marca, modelo, ano, precio])
        self.entry_marca.set_text("")
        self.entry_modelo.set_text("")
        self.entry_ano.set_text("")
        self.entry_precio.set_text("")

    def eliminar_vehiculo(self, button):
        selection = self.treeview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter is None:
            self.mostrar_error("Selecciona un vehículo para eliminar.")
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
    app = VentaVehiculos()
    Gtk.main()
