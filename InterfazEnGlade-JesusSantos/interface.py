import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio
import json
import os

class GameCatalog:
    def __init__(self):
        # Cargar el archivo Glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file('main.glade')
        
        # Obtener la ventana principal
        self.window = self.builder.get_object('main_window')
        
        # Configurar la ventana principal
        self.window.set_default_size(1200, 800)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.set_resizable(True)
        
        # Obtener widgets importantes
        self.categories_list = self.builder.get_object('categories_list')
        self.games_flow = self.builder.get_object('games_flow')
        self.search_button = self.builder.get_object('search_button')
        
        # Conectar señales
        self.window.connect('destroy', Gtk.main_quit)
        self.categories_list.connect('row-selected', self.on_category_selected)
        self.search_button.connect('clicked', self.on_search_clicked)
        
        # Cargar datos de juegos
        self.games_data = self.load_games_data()
        
        # Aplicar tema oscuro
        self.apply_dark_theme()
        
        # Mostrar todos los juegos inicialmente
        self.show_all_games()
        
        # Mostrar la ventana
        self.window.show_all()
        self.window.present()  # Asegura que la ventana esté en primer plano
    
    def load_games_data(self):
        # Datos de ejemplo (en una aplicación real, esto vendría de una base de datos o API)
        return {
            "Acción": [
                {"title": "God of War", "image": "god_of_war.jpg", "description": "Aventura épica de acción"},
                {"title": "Devil May Cry 5", "image": "dmc5.jpg", "description": "Hack and slash intenso"},
                {"title": "Doom Eternal", "image": "doom.jpg", "description": "FPS frenético"}
            ],
            "Aventura": [
                {"title": "The Legend of Zelda", "image": "zelda.jpg", "description": "Aventura épica"},
                {"title": "Red Dead Redemption 2", "image": "rdr2.jpg", "description": "Western abierto"},
                {"title": "Horizon Zero Dawn", "image": "horizon.jpg", "description": "Mundo post-apocalíptico"}
            ],
            "RPG": [
                {"title": "Final Fantasy XVI", "image": "ff16.jpg", "description": "RPG japonés"},
                {"title": "The Witcher 3", "image": "witcher.jpg", "description": "RPG de mundo abierto"},
                {"title": "Elden Ring", "image": "elden.jpg", "description": "RPG de acción"}
            ],
            "Estrategia": [
                {"title": "Civilization VI", "image": "civ6.jpg", "description": "Estrategia por turnos"},
                {"title": "Total War: Warhammer", "image": "totalwar.jpg", "description": "Estrategia en tiempo real"},
                {"title": "XCOM 2", "image": "xcom.jpg", "description": "Estrategia táctica"}
            ],
            "Deportes": [
                {"title": "FIFA 24", "image": "fifa.jpg", "description": "Fútbol"},
                {"title": "NBA 2K24", "image": "nba.jpg", "description": "Baloncesto"},
                {"title": "F1 2023", "image": "f1.jpg", "description": "Carreras"}
            ]
        }
    
    def create_game_card(self, game):
        # Crear un frame para cada juego
        frame = Gtk.Frame()
        frame.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
        
        # Contenedor vertical para la información del juego
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        box.set_margin_start(5)
        box.set_margin_end(5)
        box.set_margin_top(5)
        box.set_margin_bottom(5)
        
        # Imagen del juego (placeholder por ahora)
        image = Gtk.Image()
        image.set_from_icon_name("applications-games", Gtk.IconSize.DIALOG)
        image.set_pixel_size(128)
        box.pack_start(image, True, True, 0)
        
        # Título del juego
        title = Gtk.Label(label=game["title"])
        title.set_line_wrap(True)
        title.set_justify(Gtk.Justification.CENTER)
        box.pack_start(title, False, False, 0)
        
        # Descripción del juego
        desc = Gtk.Label(label=game["description"])
        desc.set_line_wrap(True)
        desc.set_justify(Gtk.Justification.CENTER)
        box.pack_start(desc, False, False, 0)
        
        frame.add(box)
        return frame
    
    def show_games_by_category(self, category):
        # Limpiar el FlowBox actual
        for child in self.games_flow.get_children():
            self.games_flow.remove(child)
        
        # Mostrar juegos de la categoría seleccionada
        if category in self.games_data:
            for game in self.games_data[category]:
                card = self.create_game_card(game)
                self.games_flow.add(card)
        
        self.games_flow.show_all()
    
    def show_all_games(self):
        # Limpiar el FlowBox actual
        for child in self.games_flow.get_children():
            self.games_flow.remove(child)
        
        # Mostrar todos los juegos
        for category in self.games_data.values():
            for game in category:
                card = self.create_game_card(game)
                self.games_flow.add(card)
        
        self.games_flow.show_all()
    
    def on_category_selected(self, listbox, row):
        if row is not None:
            category = row.get_child().get_text()
            self.show_games_by_category(category)
    
    def on_search_clicked(self, button):
        # TODO: Implementar búsqueda
        pass
    
    def apply_dark_theme(self):
        # Aplicar tema oscuro
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-application-prefer-dark-theme", True)
        
        # Asegurar que los colores del tema se apliquen correctamente
        style_context = self.window.get_style_context()
        style_context.add_class("dark")

if __name__ == '__main__':
    # Crear y mostrar la ventana principal
    catalog = GameCatalog()
    Gtk.main() 