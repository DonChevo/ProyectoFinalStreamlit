# 📊 Producto Analítico: Análisis de Renovación de Pólizas de Seguro

Este proyecto consiste en el desarrollo de una aplicación interactiva orientada al **Análisis Exploratorio de Datos (EDA)** del dataset *InsuranceCompany.csv*. El objetivo principal no es construir modelos predictivos, sino aplicar conceptos analíticos integrados para comprender los factores clave que influyen en la decisión de renovación de una póliza de seguro, utilizando la variable `renewal` como foco estratégico de negocio.

La aplicación está desarrollada con el paradigma de **Programación Orientada a Objetos (POO)** en el backend y una interfaz moderna e interactiva en el frontend.

---

## 🛠️ Tecnologías y Conceptos Aplicados
*   **Lenguaje:** Python
*   **Interfaz Gráfica:** Streamlit (`sidebar`, `tabs`, `columns`, `widgets` interactivos)
*   **Manipulación de Datos:** NumPy y Pandas
*   **Visualización de Datos:** Matplotlib y Seaborn
*   **Análisis Estadístico:** Estadística descriptiva, variables cualitativas/cuantitativas y análisis bivariado.
*   **Buenas Prácticas:** Programación Orientada a Objetos (POO), modularidad y manejo de estados con `st.session_state`.

---

## 📂 Estructura del Proyecto

```text
ProyectoFinalStreamlit/
├── InsuranceCompany.csv     # El dataset de prueba de la compañía de seguros
├── README.md                # Descripción del proyecto, capturas e instrucciones
├── app.py                   # Archivo principal que ejecuta la aplicación de Streamlit
├── requirements.txt         # Lista de librerías y dependencias del entorno
└── src/                     # Carpeta para el código fuente y lógica de negocio
    ├── __init__.py          # Convierte la carpeta src en un paquete de Python
    └── analyzer.py          # Clase DataProcessor (POO) y lógica analítica del EDA
```

---

## 🚀 Instrucciones de Ejecución Local

Si deseas clonar este repositorio y ejecutar la aplicación en tu entorno local, sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com
   cd ProyectoFinalStreamlit
   ```

2. **Instala las dependencias obligatorias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación de Streamlit:**
   ```bash
   streamlit run app.py
   ```

---

## 🏛️ Organización de los Módulos de la App

*   **Módulo 1 (Home):** Presentación del proyecto, tecnologías utilizadas, contexto del negocio de seguros y datos del autor.
*   **Módulo 2 (Carga del dataset):** Carga dinámica de archivos CSV con validación de datos en tiempo real y vista previa de registros.
*   **Módulo 3 (EDA):** Panel interactivo con 10 ítems de análisis (distribuciones univariadas, correlaciones paramétricas dinámicas y análisis cruzados contra la variable objetivo).
*   **Módulo 4 (Conclusiones):** 5 insights estratégicos orientados puramente a la toma de decisiones comerciales.

---

## 🔗 Enlaces del Proyecto
*   **Repositorio en GitHub:** https://github.com/DonChevo/ProyectoFinalStreamlit
*   **Aplicación Desplegada:** https://primerproyectodeportafolioprofesional.streamlit.app
