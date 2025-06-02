# Cupcake Login

## Descripción
Interfaz de inicio de sesión desarrollada con **Glade**, **GTK+3** y **PyGObject**, que permite a los usuarios acceder a un sistema con credenciales. La pantalla de autenticación incluye:
- **Etiqueta de bienvenida**
- **Campo de usuario**
- **Campo de contraseña**
- **Botón de inicio de sesión**
- **Botón para recuperar contraseña**
- **Opciones de inicio de sesión con Google y Facebook**

## Instalación
Para ejecutar este proyecto, sigue estos pasos:

### 1. Instalación de dependencias
Abre la terminal MSYS2 y ejecuta los siguientes comandos:

```sh
# Actualizar dependencias
pacman -Syu

# Instalar GTK+3
pacman -S mingw-w64-x86_64-gtk3

# Instalar Python
pacman -S mingw-w64-x86_64-python

# Instalar PyGObject
pacman -S mingw-w64-x86_64-python-pygobject
```

### 2. Configurar el PATH (Opcional)
Si Python o GTK+3 no son reconocidos después de la instalación, agrégalos al PATH:

#### Configurar el PATH para Python
Si Python no es detectado después de la instalación:

```sh
export PATH=/mingw64/bin:$PATH
```
Para que el cambio sea permanente:

```sh
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

#### Configurar el PATH para GTK+3
Si GTK+3 no es reconocido después de la instalación:

```sh
export PATH=/mingw64/bin:$PATH
```
Para que el cambio sea permanente:

```sh
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Desarrollo en Glade y Python

### Creación de la interfaz con Glade
Para diseñar la interfaz de inicio de sesión en **Glade**, se ha creado:

- **Una ventana `GtkWindow`** llamada `cupcake`, que contiene:
  - **Un `GtkLabel`** con un mensaje de bienvenida.
  - **Un `GtkTable`** donde se organizan los campos de usuario y contraseña.
  - **Un botón de inicio de sesión (`GtkButton`)** para autenticar al usuario.
  - **Un `GtkLinkButton`** para recuperar la contraseña.
  - **Botones de inicio de sesión alternativo con Google y Facebook.**

### Implementación en Python con PyGObject
El código en **Python** carga y gestiona la interfaz con **PyGObject**:

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyApp:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("cupcake.glade")  # Cargar el archivo Glade
        self.window = self.builder.get_object("cupcake")  # Obtener la ventana principal
        self.window.connect("destroy", Gtk.main_quit)  # Cerrar correctamente la ventana
        self.window.show_all()  # Mostrar la ventana completa

if __name__ == "__main__":
    app = MyApp()
    Gtk.main()
```

Este código permite cargar la interfaz desde **Glade** y manejar los eventos necesarios para el inicio de sesión.

