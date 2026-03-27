import math
import numpy as np


def mean(data):
    return sum(data) / len(data)

def median(data):
    # Usamos la libreria de numpy para calcular la media del array de datos
    return np.median(data)
    
def std_dev(data):
    mean = sum(data)/len(data)
    variance = sum((x-mean)**2 for x in data)/len(data)
    return variance **0.5
