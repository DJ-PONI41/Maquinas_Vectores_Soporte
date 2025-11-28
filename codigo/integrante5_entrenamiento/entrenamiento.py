# INTEGRANTE 5 — LUIS FERNANDO
# Entrenamiento del modelo SVM y generación de predicciones

from codigo.integrante4_preparacion_dataset.preparacion import prepare_data
from sklearn.svm import SVC
import numpy as np
from pathlib import Path

# Carpeta para guardar artefactos
ARTIFACTS_DIR = Path("artifacts")
ARTIFACTS_DIR.mkdir(exist_ok=True)


def train_and_save():
    # 1. Obtener los datos preparados por el Integrante 4
    X_train, X_test, y_train, y_test, scaler = prepare_data()

    # 2. Crear el modelo SVM con kernel RBF (más usado)
    model = SVC(kernel="rbf")

    # 3. Entrenar el modelo
    model.fit(X_train, y_train)

    # 4. Realizar predicciones
    y_pred = model.predict(X_test)

    # 5. Guardar predicciones y labels reales para los siguientes integrantes
    np.save(ARTIFACTS_DIR / "y_pred.npy", y_pred)
    np.save(ARTIFACTS_DIR / "y_test.npy", y_test)

    print("Modelo entrenado correctamente.")
    print("Predicciones generadas y guardadas en /artifacts/")
    print("Ejemplo de predicción:", y_pred[:5])

    # Retornar valores por si main.py quiere usarlos internamente
    return model, y_pred, y_test


if __name__ == "__main__":
    # Permite ejecutar este script de forma independiente
    train_and_save()
