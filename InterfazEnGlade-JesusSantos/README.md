# Catálogo de Videojuegos

Una aplicación de escritorio para visualizar y organizar un catálogo de videojuegos, desarrollada con GTK3 y Python.

## Características

- Interfaz moderna con tema oscuro
- Categorización de juegos por género
- Visualización en formato de tarjetas
- Panel lateral para navegación rápida
- Diseño responsive que se adapta al tamaño de la ventana

## Requisitos Previos

Para ejecutar esta aplicación, necesitas tener instalado:

1. MSYS2 (para Windows)
2. Python 3.x
3. GTK3 y PyGObject

## Instalación

### 1. Instalar MSYS2

1. Descarga MSYS2 desde [https://www.msys2.org/](https://www.msys2.org/)
2. Ejecuta el instalador y sigue las instrucciones
3. Abre "MSYS2 MINGW64" desde el menú de inicio

### 2. Instalar Dependencias

En la terminal de MSYS2 MINGW64, ejecuta los siguientes comandos:

```bash
# Actualizar el sistema
pacman -Syu

# Instalar GTK3 y PyGObject
pacman -S mingw-w64-x86_64-gtk3
pacman -S mingw-w64-x86_64-python-gobject
```

## Estructura del Proyecto

```
proyecto/
├── interface.py      # Código principal de la aplicación
├── main.glade       # Archivo de interfaz gráfica
└── README.md        # Este archivo
```

## Ejecución

1. Abre "MSYS2 MINGW64" desde el menú de inicio
2. Navega hasta el directorio del proyecto:
   ```bash
   cd /ruta/a/tu/proyecto
   ```
3. Ejecuta la aplicación:
   ```bash
   python3 interface.py
   ```

## Uso

- **Panel Lateral**: Selecciona una categoría para filtrar los juegos
- **Tarjetas de Juegos**: Muestra información básica de cada juego
- **Botón de Búsqueda**: (Funcionalidad pendiente de implementar)

## Categorías Disponibles

- Acción
- Aventura
- RPG
- Estrategia
- Deportes

## Personalización

### Agregar Nuevos Juegos

Para agregar nuevos juegos, modifica el diccionario `games_data` en `interface.py`. Cada juego debe tener:

```python
{
    "title": "Nombre del Juego",
    "image": "ruta/a/imagen.jpg",
    "description": "Descripción del juego"
}
```

### Modificar la Interfaz

La interfaz gráfica se puede modificar usando Glade (editor de interfaces GTK):

1. Instala Glade:
   ```bash
   pacman -S mingw-w64-x86_64-glade
   ```
2. Abre `main.glade` con Glade
3. Realiza los cambios deseados
4. Guarda y ejecuta la aplicación

## Solución de Problemas

### La ventana no se muestra correctamente

Si la ventana aparece en una esquina o no se muestra bien:
1. Asegúrate de estar usando MSYS2 MINGW64
2. Verifica que GTK3 esté instalado correctamente
3. Intenta ejecutar la aplicación nuevamente

### Errores de Importación

Si ves errores como "No module named 'gi'":
1. Verifica que PyGObject esté instalado
2. Asegúrate de estar usando Python desde MSYS2 MINGW64

## Contribuir

Siéntete libre de:
- Reportar bugs
- Sugerir nuevas características
- Enviar pull requests

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 