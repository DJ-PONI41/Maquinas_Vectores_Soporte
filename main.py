# main.py
# EJECUTA TODO EL PROYECTO AUTOMÁTICAMENTE
# 1. Preparar datos
# 2. Entrenar modelo SVM
# 3. Calcular métricas
# 4. Mostrar matriz de confusión

# Importante: Para que funcione primero todas las partes deben de estar completas

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Importar módulos del proyecto
from codigo.integrante4_preparacion_dataset.preparacion import prepare_data
from codigo.integrante5_entrenamiento.entrenamiento import train_and_save
from codigo.integrante6_metricas.metricas import load_predictions, print_metrics
from codigo.integrante7_confusion_matrix.confusion import plot_confusion

def main():
    print("===================================")
    print("  PROYECTO COMPLETO SVM - EJECUCIÓN")
    print("===================================\n")

    # 1) Preparar datos
    print("🔹 Paso 1: Preparando datos...")
    X_train, X_test, y_train, y_test, scaler = prepare_data()
    print("   Datos listos.\n")

    # 2) Entrenar modelo (este paso guarda artefactos)
    print("🔹 Paso 2: Entrenando SVM...")
    train_and_save()
    print("   Modelo entrenado y artefactos guardados.\n")

    # 3) Métricas
    print("🔹 Paso 3: Calculando métricas...")
    print_metrics()

    # 4) Matriz de confusión
    print("\n🔹 Paso 4: Mostrando matriz de confusión...")
    plot_confusion()

    print("\n===================================")
    print("       EJECUCIÓN COMPLETADA")
    print("===================================\n")

if __name__ == "__main__":
    main()
