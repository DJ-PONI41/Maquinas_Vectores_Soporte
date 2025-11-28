# 🧠 Proyecto Machine Learning con SVM

Implementación completa de un modelo de **Support Vector Machine (SVM)** aplicado al dataset **Iris**, siguiendo un flujo profesional de Machine Learning desde la preparación de datos hasta la evaluación del modelo.

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Flujo del Proyecto](#-flujo-del-proyecto)
- [Interpretación de Resultados](#-interpretación-de-resultados)
- [Equipo de Desarrollo](#-equipo-de-desarrollo)

---

## 🎯 Descripción del Proyecto

Este proyecto implementa un pipeline completo de Machine Learning que incluye:

- ✅ Preparación y normalización de datos
- ✅ Entrenamiento de modelo SVM con kernel RBF
- ✅ Evaluación mediante métricas (Accuracy, Precision, Recall, F1-Score)
- ✅ Visualización con matriz de confusión

**Dataset utilizado:** Iris (150 muestras, 4 características, 3 clases de flores)

---

## 📂 Estructura del Repositorio

```
proyecto-svm/
│
├── codigo/
│   ├── integrante4_preparacion_dataset/
│   │   └── preparacion.py
│   ├── integrante5_entrenamiento/
│   │   └── entrenamiento.py
│   ├── integrante6_metricas/
│   │   └── metricas.py
│   └── integrante7_confusion_matrix/
│       └── confusion.py
│
├── artifacts/                    # Generada automáticamente
│   ├── y_pred.npy
│   └── y_test.npy
│
├── main.py                       # Ejecuta el proyecto completo
├── requirements.txt
└── README.md
```

---

## 🔧 Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd proyecto-svm
```

### 2. Crear entorno virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Verás `(venv)` al inicio de tu terminal cuando esté activo.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Paquetes incluidos:**
- scikit-learn
- numpy
- matplotlib
- seaborn
- joblib

---

## 🚀 Ejecución

### Opción 1: Ejecutar proyecto completo (recomendado)

```bash
python main.py
```

Esto ejecuta automáticamente los 4 pasos del pipeline.

### Opción 2: Ejecutar módulos individuales

```bash
# Paso 1: Preparación de datos
python codigo/integrante4_preparacion_dataset/preparacion.py

# Paso 2: Entrenamiento del modelo
python codigo/integrante5_entrenamiento/entrenamiento.py

# Paso 3: Cálculo de métricas
python codigo/integrante6_metricas/metricas.py

# Paso 4: Matriz de confusión
python codigo/integrante7_confusion_matrix/confusion.py
```

---

## 🔄 Flujo del Proyecto

```
1. Carga del Dataset Iris
         ↓
2. División Train (70%) / Test (30%)
         ↓
3. Normalización (StandardScaler)
         ↓
4. Entrenamiento SVM (kernel RBF)
         ↓
5. Generación de Predicciones
         ↓
6. Cálculo de Métricas
         ↓
7. Visualización (Matriz de Confusión)
```

---

## 📊 Interpretación de Resultados

### Salida en Consola

Al ejecutar `main.py`, obtendrás:

```
===================================
  PROYECTO COMPLETO SVM - EJECUCIÓN
===================================

🔹 Paso 1: Preparando datos...
   Datos listos.

🔹 Paso 2: Entrenando SVM...
Modelo entrenado correctamente.
Predicciones guardadas en /artifacts/
Ejemplo de predicción: [1 0 2 1 1]

🔹 Paso 3: Calculando métricas...
=== MÉTRICAS DEL MODELO SVM ===

Accuracy: 1.0000

              precision    recall  f1-score   support
           0     1.0000    1.0000    1.0000        19
           1     1.0000    1.0000    1.0000        13
           2     1.0000    1.0000    1.0000        13

🔹 Paso 4: Mostrando matriz de confusión...
[Se abre ventana con gráfico]

===================================
       EJECUCIÓN COMPLETADA
===================================
```

### Explicación de Métricas

| Métrica | Descripción | Valor Esperado |
|---------|-------------|----------------|
| **Accuracy** | Porcentaje de predicciones correctas | 1.0 = 100% |
| **Precision** | Exactitud de predicciones por clase | 1.0 = Sin falsos positivos |
| **Recall** | Capacidad de detectar cada clase | 1.0 = Sin falsos negativos |
| **F1-Score** | Balance entre Precision y Recall | 1.0 = Modelo perfecto |

### Clases del Dataset Iris

- **0** → Iris Setosa
- **1** → Iris Versicolor
- **2** → Iris Virginica

### Matriz de Confusión

El gráfico muestra una matriz 3×3 donde:
- **Filas:** Clases reales
- **Columnas:** Clases predichas
- **Diagonal:** Predicciones correctas

**Resultado ideal:**
```
[[19  0  0]
 [ 0 13  0]
 [ 0  0 13]]
```

---

## ⚠️ Notas Importantes

- ❌ **No modificar** nombres de carpetas o archivos (rompe las importaciones)
- ❌ **No eliminar** la carpeta `artifacts/` (se genera automáticamente)
- ✅ Cada módulo debe mantener su función principal con `if __name__ == "__main__":`
- ✅ Ejecutar siempre desde la raíz del proyecto

---

## 👥 Equipo de Desarrollo

| Integrante | Módulo | Responsabilidad |
|------------|--------|-----------------|
| **Jorge Russell** | Preparación de Dataset | Carga, división train/test, normalización |
| **Luis Fernando** | Entrenamiento | Entrenar SVM, generar predicciones |
| **Erik Cuba** | Métricas | Calcular Accuracy, Precision, Recall, F1-Score |
| **Andrew Fernando** | Visualización | Construir y graficar matriz de confusión |

---

## 🎯 Objetivo del Proyecto

Demostrar la implementación profesional de un modelo SVM siguiendo las mejores prácticas de Machine Learning:

1. Preparación rigurosa de datos
2. Entrenamiento con parámetros óptimos
3. Evaluación exhaustiva del rendimiento
4. Visualización clara de resultados

---

## 📝 Conclusión

El modelo SVM con kernel RBF logra un desempeño perfecto (100% de accuracy) en el dataset Iris gracias a:

- ✅ Normalización adecuada de características
- ✅ Dataset bien separado y limpio
- ✅ Kernel RBF que captura relaciones no lineales

El proyecto es completamente **reproducible** y **modular**, ideal para aprendizaje y demostración de pipelines de ML.

---