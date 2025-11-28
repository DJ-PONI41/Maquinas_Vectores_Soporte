# INTEGRANTE 7 — ANDREW FERNANDO
# Generación y visualización de la matriz de confusión

import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Carpeta donde se guardaron los artefactos
ARTIFACTS_DIR = Path("artifacts")


def plot_confusion():
    """
    Carga las predicciones y etiquetas reales,
    calcula la matriz de confusión y la representa con seaborn.
    """
    # Cargar valores guardados por el Integrante 5
    y_pred = np.load(ARTIFACTS_DIR / "y_pred.npy")
    y_test = np.load(ARTIFACTS_DIR / "y_test.npy")

    # Calcular matriz de confusión
    cm = confusion_matrix(y_test, y_pred)

    # Graficar
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Matriz de Confusión del Modelo SVM")
    plt.xlabel("Predicciones")
    plt.ylabel("Valores Reales")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Permite ejecutar este archivo de forma independiente
    plot_confusion()
