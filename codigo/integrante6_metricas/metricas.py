# INTEGRANTE 6 — ERIK CUBA
# Cálculo de métricas del modelo SVM (accuracy, precision, recall, f1-score)

import numpy as np
from sklearn.metrics import classification_report, accuracy_score
from pathlib import Path

# Carpeta donde se guardaron los artefactos
ARTIFACTS_DIR = Path("artifacts")


def load_predictions():
    """
    Carga los archivos guardados por el Integrante 5:
    - y_pred.npy : predicciones del modelo SVM
    - y_test.npy : etiquetas reales
    """
    y_pred = np.load(ARTIFACTS_DIR / "y_pred.npy")
    y_test = np.load(ARTIFACTS_DIR / "y_test.npy")
    return y_test, y_pred


def print_metrics():
    """
    Calcula e imprime las métricas principales:
    - Accuracy
    - Precision
    - Recall
    - F1-Score
    """
    y_test, y_pred = load_predictions()

    print("=== MÉTRICAS DEL MODELO SVM ===\n")

    # Accuracy
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")

    # Classification report (precision, recall, f1-score)
    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred, digits=4))


if __name__ == "__main__":
    # Permite ejecutar este archivo por separado
    print_metrics()
