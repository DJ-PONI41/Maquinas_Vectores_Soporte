# 🚀 README - Script Principal de Ejecución (main.py)

## ⚠️ REQUISITO CRÍTICO ANTES DE EJECUTAR

**ESTE SCRIPT SOLO FUNCIONARÁ SI TODAS LAS PARTES DEL PROYECTO ESTÁN COMPLETAS**

Antes de ejecutar `main.py`, verifica que los siguientes módulos estén implementados y funcionales:

- ✅ **Integrante 4** - Preparación del dataset (`preparacion.py`)
- ✅ **Integrante 5** - Entrenamiento del modelo SVM (`entrenamiento.py`)
- ✅ **Integrante 6** - Cálculo de métricas (`metricas.py`)
- ✅ **Integrante 7** - Matriz de confusión (`confusion.py`)

Si falta algún módulo o función, el script fallará con errores de importación.

---

## 📋 Índice

1. [¿Qué hace este script?](#-qué-hace-este-script)
2. [Estructura requerida del proyecto](#-estructura-requerida-del-proyecto)
3. [Funciones que debe tener cada módulo](#-funciones-que-debe-tener-cada-módulo)
4. [Cómo ejecutar el script](#-cómo-ejecutar-el-script)
5. [Flujo de ejecución](#-flujo-de-ejecución)
6. [Verificación previa](#-verificación-previa)
7. [Solución de problemas](#-solución-de-problemas)

---

## 🎯 ¿Qué hace este script?

`main.py` es el **punto de entrada único** del proyecto que automatiza todo el pipeline de Machine Learning:

```
Preparar Datos → Entrenar SVM → Calcular Métricas → Mostrar Matriz de Confusión
```

### Ventajas:
- ✅ Ejecuta todo el proyecto con un solo comando
- ✅ Coordina automáticamente todos los módulos
- ✅ Muestra el progreso paso a paso
- ✅ Garantiza que los módulos se ejecuten en el orden correcto

---

## 📂 Estructura requerida del proyecto

Para que `main.py` funcione, la estructura debe ser **EXACTAMENTE** así:

```
proyecto/
│
├── main.py                          # ← Script principal
│
├── codigo/
│   ├── integrante4_preparacion_dataset/
│   │   └── preparacion.py          # ← Debe tener prepare_data()
│   │
│   ├── integrante5_entrenamiento/
│   │   └── entrenamiento.py        # ← Debe tener train_and_save()
│   │
│   ├── integrante6_metricas/
│   │   └── metricas.py             # ← Debe tener load_predictions() y print_metrics()
│   │
│   └── integrante7_confusion_matrix/
│       └── confusion.py            # ← Debe tener plot_confusion()
│
├── modelos/                         # ← Se crea automáticamente
├── predicciones/                    # ← Se crea automáticamente
└── requirements.txt
```

---

## 🧩 Funciones que debe tener cada módulo

### **Integrante 4: `preparacion.py`**

```python
def prepare_data():
    """
    Prepara y divide el dataset.
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test, scaler)
    """
    # Implementación...
    return X_train, X_test, y_train, y_test, scaler
```

### **Integrante 5: `entrenamiento.py`**

```python
def train_and_save():
    """
    Entrena el modelo SVM y guarda:
    - El modelo entrenado
    - Las predicciones
    - El scaler
    """
    # Implementación...
    # Guarda modelo en: modelos/svm_model.pkl
    # Guarda predicciones en: predicciones/predictions.npz
```

### **Integrante 6: `metricas.py`**

```python
def load_predictions():
    """
    Carga las predicciones guardadas.
    
    Returns:
        tuple: (y_test, y_pred)
    """
    # Implementación...
    return y_test, y_pred

def print_metrics():
    """
    Calcula e imprime:
    - Accuracy
    - Precision
    - Recall
    - F1-Score
    """
    # Implementación...
```

### **Integrante 7: `confusion.py`**

```python
def plot_confusion():
    """
    Genera y muestra la matriz de confusión.
    """
    # Implementación...
    # Muestra gráfica con plt.show()
```

---

## ▶️ Cómo ejecutar el script

### Paso 1: Activar el entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/macOS:**
```bash
source venv/bin/activate
```

### Paso 2: Instalar dependencias (si no lo has hecho)

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar main.py

```bash
python main.py
```

---

## 🔄 Flujo de ejecución

Cuando ejecutas `main.py`, verás la siguiente salida:

```
===================================
  PROYECTO COMPLETO SVM - EJECUCIÓN
===================================

🔹 Paso 1: Preparando datos...
   Datos listos.

🔹 Paso 2: Entrenando SVM...
   Modelo entrenado y artefactos guardados.

🔹 Paso 3: Calculando métricas...
   Accuracy: 0.9500
   Precision: 0.9480
   Recall: 0.9520
   F1-Score: 0.9500

🔹 Paso 4: Mostrando matriz de confusión...
[Se abre una ventana con la matriz de confusión]

===================================
       EJECUCIÓN COMPLETADA
===================================
```

### ¿Qué sucede en cada paso?

| Paso | Módulo | Acción | Archivos generados |
|------|--------|--------|-------------------|
| 1️⃣ | `preparacion.py` | Carga y prepara el dataset | Ninguno |
| 2️⃣ | `entrenamiento.py` | Entrena SVM y guarda modelo | `modelos/svm_model.pkl`<br>`predicciones/predictions.npz` |
| 3️⃣ | `metricas.py` | Carga predicciones y calcula métricas | Ninguno (solo imprime) |
| 4️⃣ | `confusion.py` | Genera matriz de confusión | Ninguno (muestra gráfica) |

---

## ✔️ Verificación previa

Antes de ejecutar `main.py`, verifica que cada módulo funcione individualmente:

### Test 1: Preparación de datos
```python
from codigo.integrante4_preparacion_dataset.preparacion import prepare_data
X_train, X_test, y_train, y_test, scaler = prepare_data()
print("✓ Preparación funciona")
```

### Test 2: Entrenamiento
```python
from codigo.integrante5_entrenamiento.entrenamiento import train_and_save
train_and_save()
print("✓ Entrenamiento funciona")
```

### Test 3: Métricas
```python
from codigo.integrante6_metricas.metricas import print_metrics
print_metrics()
print("✓ Métricas funciona")
```

### Test 4: Matriz de confusión
```python
from codigo.integrante7_confusion_matrix.confusion import plot_confusion
plot_confusion()
print("✓ Matriz de confusión funciona")
```

Si todos los tests pasan → `main.py` funcionará correctamente.

---

## 🔍 Solución de problemas

### Error: `ModuleNotFoundError: No module named 'codigo'`

**Causa:** Estás ejecutando el script desde una ubicación incorrecta.

**Solución:** Asegúrate de ejecutar `main.py` desde la raíz del proyecto:
```bash
cd /ruta/al/proyecto
python main.py
```

---

### Error: `ImportError: cannot import name 'prepare_data'`

**Causa:** Falta implementar la función `prepare_data()` en `preparacion.py`.

**Solución:** 
1. Abre `codigo/integrante4_preparacion_dataset/preparacion.py`
2. Verifica que la función `prepare_data()` exista y esté correctamente definida

---

### Error: `FileNotFoundError: modelos/svm_model.pkl`

**Causa:** El paso 2 (entrenamiento) no guardó correctamente el modelo.

**Solución:**
1. Verifica que `train_and_save()` cree la carpeta `modelos/`
2. Verifica que guarde el archivo `svm_model.pkl`

---

### Error: `No module named 'sklearn'`

**Causa:** Las dependencias no están instaladas.

**Solución:**
```bash
pip install -r requirements.txt
```

---

### La matriz de confusión no se muestra

**Causa:** La función `plot_confusion()` no llama a `plt.show()`.

**Solución:**
1. Abre `codigo/integrante7_confusion_matrix/confusion.py`
2. Asegúrate de que al final de la función haya:
```python
plt.show()
```

---

## 📊 Archivos generados después de la ejecución

Después de ejecutar `main.py` exitosamente, deberías tener:

```
proyecto/
├── modelos/
│   ├── svm_model.pkl        # Modelo entrenado
│   └── scaler.pkl           # Escalador (opcional)
│
└── predicciones/
    └── predictions.npz      # y_test y y_pred guardados
```

---

## 🎓 Buenas prácticas

1. **Ejecuta main.py solo cuando todos los módulos estén listos**
   - No lo uses para debugging de módulos individuales
   - Usa los tests individuales para cada módulo

2. **Mantén la estructura de carpetas**
   - No cambies nombres ni ubicaciones
   - Facilita la colaboración entre integrantes

3. **Versiona los cambios**
   - Usa Git para controlar versiones
   - Cada integrante trabaja en su módulo

4. **Documenta cambios importantes**
   - Si modificas interfaces de funciones, avisa al equipo

---

## 📞 Coordinación del equipo

Para que `main.py` funcione, los integrantes deben coordinarse:

| Integrante | Responsabilidad | Output esperado |
|------------|-----------------|-----------------|
| **Integrante 4** | Implementar `prepare_data()` | Retornar tupla con datos |
| **Integrante 5** | Implementar `train_and_save()` | Guardar modelo y predicciones |
| **Integrante 6** | Implementar `print_metrics()` | Imprimir métricas en consola |
| **Integrante 7** | Implementar `plot_confusion()` | Mostrar gráfica |

---

## 🎉 Resultado final

Si todo funciona correctamente, al ejecutar `main.py`:

✅ Los datos se preparan automáticamente  
✅ El modelo SVM se entrena y guarda  
✅ Las métricas se calculan y muestran  
✅ La matriz de confusión se visualiza  

**Todo el pipeline de ML ejecutado con un solo comando.**

---

## 📝 Checklist antes de ejecutar

- [ ] Todos los módulos están implementados
- [ ] El entorno virtual está activado
- [ ] Las dependencias están instaladas
- [ ] La estructura de carpetas es correcta
- [ ] Los tests individuales pasan
- [ ] Estás en la raíz del proyecto

---

**Última actualización:** Noviembre 2025