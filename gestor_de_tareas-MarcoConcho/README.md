# Gestor de Tareas

## Descripción
Gestor de tareas desarrollado con **Glade**, **GTK+3** y **PyGObject**, que permite crear, editar y eliminar tareas. Cada tarea contiene:
- **Título**
- **Descripción**
- **Fecha**
- **Prioridad**
- **Estado**

## Instalación
Para ejecutar este proyecto, sigue estos pasos:

### 1. Instalación de dependencias
Abre la terminal MSYS2 y ejecuta los siguientes comandos:

bash
# Actualizar dependencias
pacman -Syu

# Instalar GTK+3
pacman -S mingw-w64-x86_64-gtk3

# Instalar Python
pacman -S mingw-w64-x86_64-python

# Instalar PyGObject
pacman -S mingw-w64-x86_64-python-pygobject

### 2. Configurar el PATH (Opcional)
Si después de la instalación **Python** o **GTK+3** no son reconocidos en la terminal, es posible que debas agregarlos al `PATH`. Usa los siguientes comandos:

#### Exportar variables temporalmente (para la sesión actual)
bash
export PATH=/mingw64/bin:$PATH

#### Hacer el cambio permanente (se guarda en el perfil de usuario)
bash
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.baPythone ~GTK+3

Este paso asegura que Python y GTK+3 sean accesibles en todas las futuras sesiones de terminal.


## Desarrollo en Glade y Python

### Creación de la interfaz con Glade
Para desarrollar la interfaz del gestor de tareas, se utilizó Glade en Windows. La estructura principal de la ventana se diseñó con:

- **Un `Window` principal** llamado `gestor de tareas`, que sirve como la ventana de la aplicación.
- **Un `Vertical Pane`** que divide la interfaz en dos secciones:
  - **Parte superior**:
    - Contiene un `ButtonBox` con los botones:
      - **Nueva tarea**: Para agregar nuevas tareas.
      - **Editar tarea**: Para modificar una tarea existente.
  - **Parte inferior**:
    - Contiene un `Horizontal Pane` dividido en dos partes:
      - **Sección de tareas** (`Vertical Box`): Donde se almacenan las tareas creadas por el usuario.
      - **Sección de edición de tareas** (`Horizontal Box`): Aquí están los elementos que permiten ingresar los datos de cada tarea:
        - **`TextEntry`**: Para el **título** y la **descripción** de la tarea.
        - **`ComboBox`**: Para seleccionar la **prioridad** y el **estado** de la tarea.
        - **`Calendario`**: Para establecer la fecha de la tarea.
        - **Botón de guardar**: Ubicado debajo de la descripción, para almacenar los cambios de la tarea.

### Implementación en Python con PyGObject
Una vez diseñada la interfaz en Glade, se creó el código en Python utilizando PyGObject para conectarla con la lógica de la aplicación.

1. **Importación de PyGObject y configuración de GTK**:
   
python
   import gi
   gi.require_version("Gtk", "3.0")
   from gi.repository import Gtk
  

2. **Creación de la clase principal**:
   
python
   class MyApp:
       def init(self):
           builder = Gtk.Builder()  # Inicializa el builder para cargar la interfaz
           builder.add_from_file("gestor_tareas.glade")  # Carga el archivo Glade
           self.window = builder.get_object("gestor_de_tareas")  # Obtiene la ventana principal
           self.window.show_all()  # Muestra la ventana completa
  

Este código permite cargar y gestionar la interfaz del gestor de tareas, vinculando los elementos de Glade con la lógica de programación en Python.



