import json
import os
import uuid

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(DIRECTORIO_BASE, 'tareas.json')

def cargar_tareas():
    """Carga las tareas del archivo JSON. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    with open(ARCHIVO_DATOS, 'r') as file:
        return json.load(file)

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_DATOS, 'w') as file:
        json.dump(tareas, file, indent=4)

def agregar_tarea(tareas, titulo, descripcion, fecha):
    """Lógica para agregar una tarea a la lista."""
    nueva_tarea = {
        "id": str(uuid.uuid4())[:8], # Genera un ID corto de 8 caracteres
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha": fecha,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea)
    return tareas

def listar_pendientes(tareas):
    """Filtra y devuelve solo las tareas pendientes."""
    return [t for t in tareas if t['estado'] == 'pendiente']

def completar_tarea(tareas, id_tarea):
    """Busca una tarea por ID y la marca como completada."""
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            tarea['estado'] = 'completada'
            return True # Retorna True si la encontró y modificó
    return False

