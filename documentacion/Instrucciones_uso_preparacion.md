# 📘 README.md — Guía de uso del módulo de Preparación del Dataset

**Integrante 4: Jorge Russell**

Este documento explica cómo importar y utilizar correctamente el módulo de preparación del dataset. Sigue estas indicaciones para evitar errores de rutas, importaciones o dependencias.

---

## 📂 1. Estructura del proyecto

La estructura del proyecto debe ser **EXACTAMENTE** como se muestra a continuación:

```
proyecto/
│
├── codigo/
│   ├── integrante4_preparacion_dataset/
│   │   └── preparacion.py
│   │
│   ├── integrante5_entrenamiento/
│   ├── integrante6_metricas/
│   └── integrante7_confusion_matrix/
│
└── requirements.txt
```

> **⚠️ IMPORTANTE:** No cambiar nombres de carpetas ni archivos. Si se modifican, las importaciones dejarán de funcionar.

---

## 🧩 2. Contenido del módulo

El archivo **`preparacion.py`** contiene la función principal:

```python
def prepare_data():
    """
    Prepara y divide el dataset para entrenamiento y prueba.
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test, scaler)
    """
```

### Valores devueltos:

- `X_train`: Datos de entrenamiento (features)
- `X_test`: Datos de prueba (features)
- `y_train`: Etiquetas de entrenamiento
- `y_test`: Etiquetas de prueba
- `scaler`: Objeto escalador ajustado

---

## 📥 3. Importación correcta

Para usar el módulo desde cualquier parte del proyecto:

```python
from codigo.integrante4_preparacion_dataset.preparacion import prepare_data

# Obtener los datos preparados
X_train, X_test, y_train, y_test, scaler = prepare_data()
```

### ✅ Buenas prácticas:
- Usar la importación tal como se muestra arriba
- Importar directamente desde el módulo original

### ❌ Evitar:
- Copiar la función a otros archivos
- Mover o renombrar el módulo
- Modificar la estructura de carpetas

---

## 🧪 4. Prueba de importación

Crea un archivo `test_import.py` en la raíz del proyecto:

```python
from codigo.integrante4_preparacion_dataset.preparacion import prepare_data

# Cargar los datos
X_train, X_test, y_train, y_test, scaler = prepare_data()

# Verificar que todo funciona
print("✓ Importación exitosa")
print(f"Train shape: {X_train.shape}")
print(f"Test shape: {X_test.shape}")
print(f"Clases únicas: {len(set(y_train))}")
```

Ejecutar la prueba:

```bash
python test_import.py
```

**Resultados esperados:**
- ✅ Sin errores → Todo configurado correctamente
- ❌ Con errores → Revisar estructura de carpetas y nombres

---

## 🔧 5. Configuración del entorno virtual

### En Windows:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
venv\Scripts\activate
```

### En Linux / macOS:

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno
source venv/bin/activate
```

Cuando el entorno está activo, verás `(venv)` al inicio de la línea de comandos.

---

## 📦 6. Instalación de dependencias

Con el entorno virtual activado, instala las dependencias:

```bash
pip install -r requirements.txt
```

### Contenido de `requirements.txt`:

```
scikit-learn
numpy
matplotlib
seaborn
joblib
```

> **⚠️ NOTA:** Todos los integrantes deben instalar estas dependencias antes de ejecutar sus scripts.

> **⚠️ NOTA2:** Si nesesitas otras librerias extra añadelas al archivo `requirements.txt` en el mismo formato que los demas requerimientos.

---

## 🚀 7. Ejemplo de uso (Integrante 5 - Entrenamiento)

```python
from codigo.integrante4_preparacion_dataset.preparacion import prepare_data
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargar datos preparados
X_train, X_test, y_train, y_test, scaler = prepare_data()

# Entrenar modelo
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar resultados
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
```

---

## 🔍 8. Solución de problemas comunes

| Error | Causa probable | Solución |
|-------|---------------|----------|
| `ModuleNotFoundError` | Estructura de carpetas incorrecta | Verificar nombres y ubicaciones |
| `ImportError` | Entorno virtual no activado | Activar `venv` |
| `No module named 'sklearn'` | Dependencias no instaladas | Ejecutar `pip install -r requirements.txt` |
| Datos con forma incorrecta | Versión desactualizada | Actualizar `preparacion.py` |

---

## 📞 9. Contacto

Para dudas o problemas con este módulo, contactar a:

**Jorge Russell** - Integrante 4  
Responsable del módulo de preparación de datos

---

## 📝 10. Changelog

- **v1.0** - Versión inicial del módulo de preparación
- Función `prepare_data()` implementada
- Escalado y división de datos incluidos

---

**Última actualización:** Noviembre 2025