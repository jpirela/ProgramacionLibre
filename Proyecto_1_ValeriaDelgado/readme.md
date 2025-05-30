# Menú de Comida 

## ¿De qué trata este proyecto?

Este proyecto es un **Menú de Comida ** creado con **Glade**, **GTK+ 3** y **Python**. Presenta una interfaz gráfica que puede ser usada como base para sistemas de pedidos o menús digitales.

La interfaz está lista para incorporar funciones como selección de platos, precios y procesamiento de pedidos.

## Requisitos para ejecutarlo

En Windows se recomienda usar **MSYS2** para instalar las dependencias necesarias. Desde la terminal de MSYS2, se deben seguir estos pasos:

### 1. Actualizar los paquetes del sistema:

```
pacman -Syu
```

### 2. Instalar GTK+ 3:

```
pacman -S mingw-w64-x86_64-gtk3
```

### 3. Instalar Python:

```
pacman -S mingw-w64-x86_64-python
```

### 4. Instalar PyGObject (para conectar Python con GTK):

```
pacman -S mingw-w64-x86_64-python-pygobject
```

## ¿Qué hacer si no se reconoce GTK+ o Python?

Puede ser necesario modificar el **PATH** del sistema.

### Temporalmente:

```
export PATH=/mingw64/bin:$PATH
```

### Para que el cambio sea permanente:

```
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Estructura de la interfaz

La interfaz fue diseñada con **Glade** que incluye una ventana principal (`window1`) que incluye botones, cuadros de entrada y otros elementos visuales relacionados a un menú de comida.

El archivo `.glade` se puede modificar desde Glade para personalizar la interfaz.

## Conexión entre Python y la interfaz

El script `ejecutarinterfaz.py` carga y muestra la ventana del menú usando PyGObject. Este es el código utilizado:

```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def abrir_glade(archivo_glade):
    builder = Gtk.Builder()
    builder.add_from_file(archivo_glade)

    ventana = builder.get_object("window1")
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()

    Gtk.main()

abrir_glade("menucomida.glade")
```

## ¿Cómo se ejecuta?

1. Asegura que los archivos `menucomida.glade` y `ejecutarinterfaz.py` estén en la misma carpeta.
2. Abre la terminal de MSYS2 y ejecuta:

```bash
python ejecutarinterfaz.py
```