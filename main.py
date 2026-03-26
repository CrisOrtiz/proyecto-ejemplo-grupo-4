def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")

def ejecutar():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        match opcion:
            case "1":
                # Agregar tarea 1
                print("Tarea 1")
                break
            case "2":
                # Agregar tarea 2
                print("Tarea 2")
                break
            case "3":
                # Agregar tarea 3
                print("Tarea 3")
                break
            case "4":
                # Agregar tarea 4
                print("Tarea 4")
                break
            case _: 
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    ejecutar()