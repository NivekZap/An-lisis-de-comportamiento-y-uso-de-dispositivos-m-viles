import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
file_path = "dataset.csv"  # Reemplaza con la ruta del archivo
data = pd.read_csv(file_path)

# Mostrar las primeras filas
print(data.head())

# Explorar el dataset
print(data.info())
print(data.describe())

# ¿Cuáles son las columnas y su significado?
# ¿Hay valores faltantes o datos inconsistentes?
# ¿Qué tipo de análisis puede interesar a las empresas (patrones de uso, segmentos de usuarios, etc.)?
# Distribución de una variable (por ejemplo, duración de uso)
sns.histplot(data['duration'], bins=30, kde=True)
plt.title("Distribución de la duración de uso")
plt.show()

# Comparar patrones de uso entre géneros (si la columna existe)
sns.boxplot(x='gender', y='duration', data=data)
plt.title("Patrones de uso por género")
plt.show()

# Relación entre dos variables (por ejemplo, duración y edad)
sns.scatterplot(x='age', y='duration', data=data)
plt.title("Relación entre edad y duración de uso")
plt.show()










