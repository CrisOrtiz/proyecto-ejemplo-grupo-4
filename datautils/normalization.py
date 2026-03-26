from .statistics import mean, std_dev

def min_max(data):
 # Añadir implementación de normalización min-max
 print("Función min_max aún no implementada.")

# Normalización z-score
def z_score(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    normalized_data = [(x - mean) / std_dev for x in data]
    return normalized_data