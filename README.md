# Sistema de Gestión de Tareas Personal

Una aplicación de línea de comandos (CLI) construida en Python para gestionar tareas diarias de forma eficiente, almacenando la información de manera persistente en un archivo JSON.

## Funcionalidades Principales:

1. **Agregar tareas:** Permite ingresar título, descripción y fecha límite.
2. **Listar pendientes:** Visualiza rápidamente las tareas que aún no has terminado.
3. **Completar tareas:** Marca las tareas como completadas mediante un ID único generado automáticamente.

## Requisitos Técnicos Cumplidos:

- [x] Uso de Git (Mínimo 5 commits).
- [x] 2 Diagramas (Arquitectura y Flujo).
- [x] Uso del depurador (VS Code Debugger aplicado en la inserción y modificación de datos).
- [x] 3 pruebas unitarias usando unittest (test_main.py).

## Manual de Usuario Básico:

**Instalación**: Asegúrate de tener Python instalado. Clona el repositorio y abre la carpeta en tu terminal.

**Ejecución**: Escribe python main.py en tu consola.

**Uso**: 
- El sistema mostrará un menú numérico del 1 al 4.
- Escribe el número de la acción que deseas realizar y presiona Enter.
- Para completar una tarea (Opción 3), primero usa la Opción 2 para ver tus tareas pendientes y copia el ID (el código de 8 letras/números entre corchetes, ej: [a1b2c3d4]). Pega ese ID cuando el sistema te lo pida.

## Problemas Encontrados y Soluciones:

**Problema**: Al ejecutar el programa por primera vez, fallaba porque intentaba leer un archivo tareas.json que aún no existía.

**Solución**: Se implementó la librería os para verificar la existencia del archivo en la función cargar_tareas(). Si no existe os.path.exists(), el sistema devuelve automáticamente una lista vacía [] evitando el error fatal.

**Problema**: Riesgo de borrar el archivo JSON al realizar las pruebas automatizadas.

**Solución**: Se separó la lógica pura de manipulación de listas (agregar_tarea, completar_tarea) de la lógica de escritura de archivos (guardar_tareas). Así, test_main.py solo evalúa las listas en la memoria RAM sin tocar el disco duro.

**Problema**: Al cerrar y volver a abrir la terminal (o al ejecutar el programa desde una carpeta diferente), el programa no leía las tareas guardadas previamente, sino que creaba un archivo `tareas.json` nuevo y vacío. Esto se debía a un conflicto con las rutas relativas.

**Solución**: Se actualizó el código para utilizar rutas absolutas dinámicas mediante `os.path.dirname(os.path.abspath(__file__))`. Esto obliga al programa a buscar y guardar el archivo `tareas.json` exactamente en el mismo directorio donde reside el script `main.py`, asegurando que el historial de tareas se cargue correctamente sin importar desde dónde se abra la consola.

## Diagramas del Sistema

### Diagrama de Flujo
graph TD
    A[Inicio] --> B[Ingresar Datos]
    B --> C{Generar ID Único}
    C --> D[Guardar en JSON]
    D --> E[Mostrar Éxito]
    E --> F[Fin]

### Diagrama de Arquitectura

```mermaid
graph LR
    A[Usuario Consola] <--> B(main.py)
    B <--> C[(tareas.json)]