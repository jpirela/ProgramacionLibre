# ProyectoGlade1_RafaelCastro
Se descargan e instalan las aplcaciones junto con las librerias necesarias 
sudo apt update
sudo apt install glade (Interfaz de Glade)
sudo apt install sqlite3 (Base de datos)
sudo apt install python3
sudo apt install libgtk-3-dev (GTK 3)

# Post-Instalacion
Luego de haber descargado todas las tecnologias necesarias, procedi a abrir la aplicacion glade
y ya dentro cree un nuevo archivo llamado ventana en el cual desarrolle 4 ventanas con GtkWindow,
a cada ventana se le asigno un contenedor de tipo Fixed para poder manejar de manera manual la posicion de cada elemento
posteriormente ingresado. 

### Primera Ventana
En la primera ventana se puede apreciar 3 labels junto con 3 GtkEntry (Campos de Texto) donde se pueden registrar usuarios 
con su nombre, apellido y cedula y al presionar el boton de registro se guardara la informacion en una base de datos llamada configuraciones.db en la tabla Cliente. 
En la esquina superior derecha se puede apreciar un combobox con 4 colores diferentes, los cuales al ser pulsados pueden 
cambiar el color de fondo de la pantalla principal y este se guardara en otra tabla de la base de datos para poder restaurarlo la siguiente vez que se inicie la ventana. 
Luego estan otros botones que abriran 2 ventanas diferentes.

### Ventana-Productos
Una ventana contendra una descripcion general de una empresa junto con sus productos disponibles actualmente. Los productos agregados son un ejemplo de la idea de una concesionaria.
Dentro del Contenedor general GtkFixed agregue otro contenedor GtkGrid para agrupar de manera mas ordenada los labels e imagenes

### Ventana-Login
En la ventana de Login, dentro del contenedor GtkFixed añadi un contenedor GtkBox para de igual manera poder representar el contenido mas ordenado,
se puede apreciar una imagen cargada con GtkImage Con el Logo de la concesionaria en la parte superior,
en mitad de la ventana estan 2 GtkEntry con sus respectivas etiquetas donde se ingresaran un nombre y apellido, los cuales se verificara si coinciden con alguno registrado en la base de datos,
por ultimo en la parte inferior se encuentra el boton que se encargara de realizar la consulta sql y verificar que el Usuario este registrado

### Ventana-Iniciado-Sesion
Esta Ventana aun se encuentra en Desarrollo, ya que unicamente se tiene un boton que mostrara el nombre del usuario ingresado.
Se tiene como idea una ventana en donde se puedan realizar compras de vehiculos, visualizando precios, modelos entre otras cosas

### Codigo-Python
Por ultimo mediante un conjunto de archivos .py que trabajan interconectados se logra manejar las conexiones con la base de datos y las funcionalidades de todas las ventanas, como lo son
los botones, combobox, Entrys entre otros,

### Ejecutar-Programa
Para ejecutar el programa se necesitar abrir la terminal y escribir el siguiente comando dentro del fichero
python3 app.py
