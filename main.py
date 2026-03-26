from datautils import *

def mostrar_menu():
    print("\n--- Menu de medidas fundamentales ---")

def ejecutar():
    tareas = []
    data = [10, 25, 28, 40, 50]
    print("Datos:", data)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        match opcion:
            case "1":
                # Agregar tarea 1 - min_max
                print("Tarea 1")
            case "2":
                # Agregar tarea 2 - z_score
                print("Tarea 2")
            case "3":
                # Agregar tarea 3 - median
                print("Tarea 3")
            case "4":
                # Agregar tarea 4 - std_dev
                print("Tarea 4")
            case "5":
                print("Saliendo del programa...")
                break
            case _: 
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    ejecutar()