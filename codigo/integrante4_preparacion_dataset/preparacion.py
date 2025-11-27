from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from typing import Tuple
import numpy as np

def prepare_data(test_size: float = 0.3, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, StandardScaler]:
    """
    Carga el dataset Iris, divide en train/test y escala con StandardScaler.
    Retorna: X_train, X_test, y_train, y_test, scaler
    """
    # 1. Cargar el dataset
    data = datasets.load_iris()
    X = data.data
    y = data.target

    # 2. Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # 3. Normalizar los datos
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler


if __name__ == "__main__":
    # Ejecución directa para debug / demostración
    X_train, X_test, y_train, y_test, scaler = prepare_data()
    print("Ejemplo de filas (raw):")
    print(X_train[:3])
    print("Tamaño Train:", X_train.shape)
    print("Tamaño Test:", X_test.shape)

# Export público
__all__ = ["prepare_data"]
