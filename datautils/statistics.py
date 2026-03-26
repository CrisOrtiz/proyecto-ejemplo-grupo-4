import math

def mean(data):
    return sum(data) / len(data)

def median(data):
    # Añadir implementación de la mediana
    print("Función median aún no implementada.")
    
def std_dev(data):
    mean = sum(data)/len(data)
    variance = sum((x-mean)**2 for x in data)/len(data)
    return variance **0.5
