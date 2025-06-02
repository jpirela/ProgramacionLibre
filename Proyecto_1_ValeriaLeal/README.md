# Calendario de Formula 1 

Este proyecto trata sobre un calendario de la formula 1, para la parte visual utilice Glade y para ejecutarlo Python con GTK3. A continuacion, la explicacion de todo el proyecto. 

**Instalacion de la maquina virtual, Lubuntun y Glade**

Para descargar la herramienta a utilizar (glade), instale el software: Virtual Box, que es un software de virtualizacion. Luego a la maquina virtual le instale Lubuntun-24.04.2 que es una  distribucion de Linux, una version oficial de Ubuntun y Ubuntun es una distribucion de Linux que esta basada en Debian, que era lo que se requeria instalar. Luego de esta instalacion y configurar Lubuntun, fui hasta la consola y instale Glade con el siguiente comando: 

sudo snap install glade. 

Ingrese mi clave y glade se instalo correctamente. 

**Caracteristicas Visuales del calendario**

Contiene una Ventana principal, su id es: main_ventana. 

Sobre la  ventana contiene un Fixed, su id es: FixedPrincipal. Elegi utilizar un Fixed en vez de un box porque con el Fixed senti un mayor control sobre los elementos visuales que colocaria. 

En la parte superior se ubica un grid, su id es: gridPrincipal. Este grid contiene 5 columnas donde estan distribuidos distintos botones. 

A continuacion nombre, futura funcion y ID de los botones: 

Boton 1: Pilotos, su funcion es desplegar la informacion esencial de los pilotos, como nombre completo, dorsal, escuderia a la que pertenecen y pais al que representan. Su id es: botonPilotos. 

Boton 2: Equipos, su funcion es desplegar la informacion esencial de los equipos como pilotos que estan pertenecen, pais de origen y jefe de equipo. Su id es: botonEquipos. 

Boton 3: Carreras, su funcion desplegar informacion sobre las carreras como pilotos o equipos que tienen carerra en casa, nombre de la pista, horario de la carrera y record de pista. Su id es: botonCarreras.

Boton 4: Campeonato de pilotos, despliega informacion sobre como van los pilotos en la tabla de posiciones. Su id es: botonCpilotos. 

Boton 5: Campeonato de constructores, despliega informacion sobre como van los equipos en el campeonato de constructores. Su id es: BotonConstrutores. 

Mas abajo nos encontramos con dos Labels que nos dan la bienvenida cuando entramos, el primero nos informa sobre la proxima carrera, su id es: labelInfoCarrera. Luego tenemos otro Label que nos da el horario de la carrera, nombre de la pista, el record de la pista y quien lo rompio, su id es: labelInfo. En medio de los dos labels se mostrara una imagen de la pista como referencia, la imagen hasta los momentos no esta disponible y se espera agregarla cuando se comience la proximo fase del proyecto. El id de la imagen es: imagenCircuito.  

**Python**

Para compilar el programa se utilizo Python con la libreria GTK, y se le agregaron las funciones self.window.set_default_size(800, 650) para colocarle un tamaño agradable a la ventana y self.window.set_resizable(False) para que el usuario no pueda juegar con las dimensiones del programa, ademas de eso, no tiene otra funcion. 

**Recomendaciones** 

Asegurate de tener instalados los siguientes componentes: 

-GTK 3.
-Python (una version mas o menos actual deberia servir). 

**Autor/a**

Valeria Leal 31.696.367. Programacion de software libre. 