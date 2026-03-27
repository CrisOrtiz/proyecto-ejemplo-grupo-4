import math
import numpy as np


def mean(data):
    return sum(data) / len(data)

def median(data):
    # Usamos la libreria de numpy para calcular la media del array de datos
    return np.median(data)
    
def std_dev(data):
    # Añadir implementación de la desviación estándar
    print("Función std_dev aún no implementada.")