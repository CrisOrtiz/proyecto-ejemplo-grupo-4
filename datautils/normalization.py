from .statistics import mean, std_dev

def min_max(data):
  min_val = min(data)
  max_val = max(data)
  return [(x - min_val) / (max_val - min_val) for x in data]

def z_score(data):
    # Añadir implementación de normalización z-score
    print("Función z_score aún no implementada.")