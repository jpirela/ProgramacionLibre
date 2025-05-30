# 📒 Gestor de Contactos

## ¿Qué es este proyecto?

Este es un **Gestor de Contactos** desarrollado con **Glade**, **GTK+ 3** y **Python**. Permite visualizar una interfaz gráfica que en futuras versiones puede extenderse para gestionar contactos (como una agenda).

La interfaz está diseñada y lista para integrar funcionalidades como agregar, editar o eliminar contactos.


## ¿Qué se necesita para ejecutarlo?

En sistemas Windows, se recomienda utilizar **MSYS2** para instalar las herramientas necesarias. Desde la terminal de MSYS2, se deben ejecutar los siguientes comandos:

### 1. Actualizar el sistema:

```
pacman -Syu
```

### 2. Instalar GTK+ 3 (para la interfaz gráfica):

```
pacman -S mingw-w64-x86_64-gtk3
```

### 3. Instalar Python:

```
pacman -S mingw-w64-x86_64-python
```

### 4. Instalar PyGObject (permite usar GTK con Python):

```
pacman -S mingw-w64-x86_64-python-pygobject
```

## ¿Qué hacer si Python o GTK+ no se reconocen?

Puede ser necesario agregar las rutas al **PATH**.

### Para usarlo temporalmente:

```
export PATH=/mingw64/bin:$PATH
```
### Para agregarlo de forma permanente:

```
echo 'export PATH=/mingw64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## ¿Cómo está hecha la interfaz?

La interfaz fue creada con **Glade**, utilizando una estructura simple:

* Una **ventana principal** llamada `window1`.
* Elementos de interfaz como botones, entradas de texto u otros, según el diseño en Glade.

El archivo `.glade` se puede modificar en cualquier momento desde Glade para cambiar o mejorar la interfaz.


## ¿Cómo se conecta la interfaz con Python?

El archivo `ejecutarinterfaz.py` carga el archivo `.glade` y muestra la ventana usando PyGObject. El siguiente es el contenido del script:


```
python
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

abrir_glade("gestorcontactos.glade")
```



## ¿Cómo ejecutar el programa?

1. Verificar que los archivos `gestorcontactos.glade` y `ejecutarinterfaz.py` se encuentren en la misma carpeta.

2. Abrir la terminal de MSYS2 y ejecutar el comando:

```
python ejecutarinterfaz.py
```