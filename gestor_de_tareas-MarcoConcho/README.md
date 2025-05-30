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


# Actualizar dependencias
`
pacman -Syu
`
# Instalar GTK+3
`
pacman -S mingw-w64-x86_64-gtk3
`
# Instalar Python
`
pacman -S mingw-w64-x86_64-python
`
# Instalar PyGObject
`
pacman -S mingw-w64-x86_64-python-pygobject
`
### 2. Configurar el PATH (Opcional)
Si Python o GTK+3 no son reconocidos después de la instalación, debes agregarlos al PATH.  

### Configurar el PATH para Python
Si Python no es detectado después de la instalación, usa el siguiente comando en MSYS2:  

#### Exportar Python temporalmente
```
export PATH=/mingw64/bin:$PATH
Esto hará que Python sea reconocido en la sesión actual.  
```
#### Hacer el cambio permanente
Para que Python siempre esté disponible en futuras sesiones, agrégalo al archivo .bashrc con: 
```
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Configurar el PATH para GTK+3
Si GTK+3 no es reconocido después de la instalación, usa estos comandos:  

#### Exportar GTK+3 temporalmente
```
export PATH=/mingw64/bin:$PATH
```
#### Hacer el cambio permanente
Al igual que con Python, haz que el cambio sea permanente con:  
```
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```
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
```  
python
   import gi
   gi.require_version("Gtk", "3.0")
   from gi.repository import Gtk
 ``` 

2. **Creación de la clase principal**:
```
python
   def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("tareas2.glade")  # archivo

        self.window = self.builder.get_object("gestor de tareas")  # ID de la ventan
        self.window.connect("destroy", Gtk.main_quit)  # Para cerrar correctamente la ventana

        # Mostrar la ventana
        self.window.show_all()
```
  

Este código permite cargar y gestionar la interfaz del gestor de tareas, vinculando los elementos de Glade con la lógica de programación en Python.



