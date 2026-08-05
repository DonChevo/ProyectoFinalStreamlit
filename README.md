Proyecto que pide desarrollar una aplicación app.py ejecutable con Streamlit.
Aplicar conceptos fundamentales de:
• Variables y tipos de datos
• Funciones
• f-strings
• Programación Orientada a Objetos (POO)
• NumPy y Pandas
• Visualización con Matplotlib y Seaborn
• Estadística descriptiva

El dataset adjunto InsuranceCompany.csv contiene información histórica de clientes de
una compañía de seguros. Incluye variables demográficas, económicas, historial de
pagos, comportamiento de morosidad, canal de captación, tipo de residencia, valor
de la prima y puntaje de evaluación del cliente.
El objetivo principal es analizar los factores que influyen en la renovación de una
póliza de seguro, utilizando la variable renewal como variable objetivo. Este
conjunto de datos permite aplicar análisis exploratorio, visualización de datos y
modelos predictivos para identificar patrones de clientes que renuevan o no su
seguro.

ProyectoFinalStreamlit/
│
├── InsuranceCompany.csv     # El dataset
├── README.md                # Descripción del proyecto, capturas e instrucciones (Obligatorio)
├── app.py                   # Archivo principal que ejecuta la aplicación de Streamlit
├── requirements.txt         # Lista de librerías y dependencias (Obligatorio)
│
└── src/                     # Carpeta para el código fuente y lógica de negocio
    ├── __init__.py          # Convierte la carpeta src en un paquete de Python
    └── analyzer.py          # Clase DataAnalyzer/DataProcessor (POO) y lógica del EDA
