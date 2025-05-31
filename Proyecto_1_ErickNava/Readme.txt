Erick Nava / Proyecto Glade1

Instalación de Aplicaciones y Librerías Necesarias

Para comenzar el proyecto, se deben instalar las aplicaciones y librerías necesarias en Kali Linux mediante los siguientes comandos: 
primero actualizar el sistema con "sudo apt update", luego instalar Glade con "sudo apt install glade" para el editor de interfaces gráficas GTK, 
instalar Python 3 con "sudo apt install python3" y las librerías de desarrollo GTK 3 con "sudo apt install libgtk-3-dev".

Post-Instalación

Después de instalar las herramientas necesarias, se abre Glade para crear la interfaz gráfica de la aplicación. 
Se diseñó un archivo llamado "ventavehiculos.glade" que contiene la ventana principal con un formulario para agregar vehículos y una vista de inventario.

Interfaz Principal

La ventana principal consta de un formulario con los siguientes campos: Marca, Modelo, Año y Precio. El campo de precio incluye un símbolo "$" 
delante para indicar la moneda.

Además, cuenta con dos botones: "Agregar Vehículo" para añadir vehículos al inventario mostrado en una tabla, y "Eliminar Vehículo" para 
eliminar el vehículo seleccionado de dicha tabla.

El inventario se muestra en una tabla con columnas para Marca, Modelo, Año y Precio (formateado con símbolo "$" y dos decimales).

Funcionalidad del Programa

Mediante un script en Python llamado "venta_vehiculos.py", se carga la interfaz creada en Glade y se implementan las funciones para validar los campos
antes de agregar un vehículo, agregar vehículos al inventario, eliminar vehículos seleccionados, mostrar mensajes de error cuando los datos son incorrectos o faltan,
 y formatear el precio con el símbolo "$" en la tabla para mejor presentación.

El programa está basado en Gtk3 con PyGObject.

Ejecución del Programa

Para ejecutar la aplicación, se debe abrir una terminal y ejecutar el archivo Python con el comando "python3 venta_vehiculos.py". 
Esto abrirá la ventana principal donde se podrá gestionar el inventario de vehículos de forma sencilla.

