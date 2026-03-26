from datautils import *

def show_menu():
    print("\n--- Menu de medidas fundamentales ---")
    print("1. Normalización Min-Max")
    print("2. Normalización Z-Score")
    print("3. Mediana")
    print("4. Desviación Estándar") 
    print("5. Salir\n")

def run():
    data = [10, 25, 28, 40, 50]
    print("Datos:", data)

    while True:
        show_menu()
        option = input("Selecciona una opción: ")
        
        match option:
            case "1":
                # Agregar tarea 1 - min_max(data) - Cristhian
                print("Tarea 1")
            case "2":
                # Agregar tarea 2 - z_score(data) - Michael
                z_score_result = z_score(data)
                print("Resultado de z_score:", z_score_result)
            case "3":
                # Agregar tarea 3 - median(data) - Billy
                print("Tarea 3")
            case "4":
                # Agregar tarea 4 - std_dev(data) - Danna
                print("Tarea 4")
            case "5":
                print("Saliendo del programa...")
                break
            case _: 
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    run()