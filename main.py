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

def menu():
    """Interfaz de consola para el usuario."""
    tareas = cargar_tareas()
    
    while True:
        print("\n--- GESTOR DE TAREAS ---\n")
        print("1. Agregar nueva tarea")
        print("2. Ver tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Salir\n")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            desc = input("Descripción: ")
            fecha = input("Fecha límite (DD/MM/AAAA): ")
            tareas = agregar_tarea(tareas, titulo, desc, fecha)
            guardar_tareas(tareas)
            print("\nTarea agregada con éxito.")
            
        elif opcion == '2':
            pendientes = listar_pendientes(tareas)
            print("\n--- TAREAS PENDIENTES ---")
            if not pendientes:
                print("No hay tareas pendientes. ¡Buen trabajo!")
            for t in pendientes:
                print(f"[{t['id']}] {t['titulo']} (Vence: {t['fecha']}) - {t['descripcion']}")
                
        elif opcion == '3':
            pendientes = listar_pendientes(tareas)
            
            #Verificamos si hay tareas por completar
            if not pendientes:
                print("No hay tareas pendientes. ¡Buen trabajo!")
            else:
                print("\n--- Tareas Disponibles para Completar ---")
                # Mostramos un resumen rapido con ID y el titulo
                for t in pendientes:
                    print(f"[{t['id']}] {t['titulo']}")
                    
                id_tarea = input("\nIngresa el ID de la tarea a completar (o escribe 'salir' para cancelar): ")
                
                # Opcion para salir por si el usuario desea
                
                if id_tarea.lower() == 'salir':
                    print("Operacion Cancelada")
                else:
                    if completar_tarea(tareas,id_tarea):
                        guardar_tareas(tareas)
                        print("Tarea Marcada como Completada")
                    else:
                        print("Tarea no Encontrada, Revisa El ID de la Tarea e intentalo denuevo")
                    
        elif opcion == '4':
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()