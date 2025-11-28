# INTEGRANTE 5 — LUIS FERNANDO
# Entrenamiento del modelo SVM y generación de predicciones

from codigo.integrante4_preparacion_dataset.preparacion import prepare_data
from sklearn.svm import SVC
import numpy as np
from pathlib import Path

ARTIFACTS_DIR = Path("artifacts")
ARTIFACTS_DIR.mkdir(exist_ok=True)


def train_and_save():
    X_train, X_test, y_train, y_test, scaler = prepare_data()
    model = SVC(kernel="rbf")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    np.save(ARTIFACTS_DIR / "y_pred.npy", y_pred)
    np.save(ARTIFACTS_DIR / "y_test.npy", y_test)

    print("Modelo entrenado correctamente.")
    print("Predicciones generadas y guardadas en /artifacts/")
    print("Ejemplo de predicción:", y_pred[:5])
    return model, y_pred, y_test
if __name__ == "__main__":
    train_and_save()
