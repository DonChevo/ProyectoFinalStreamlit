import streamlit as pd
import streamlit as st

# Configuración de la página (Debe ser la primera directiva de Streamlit)
st.set_page_config(
    page_title="Product Analítico - Insurance Company",
    page_icon="📊",
    layout="wide",
)

# -------------------------------------------------------------------------
# SIDEBAR - MENÚ DE NAVEGACIÓN PRINCIPAL
# -------------------------------------------------------------------------
st.sidebar.title("Navegación")
opcion_menu = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        "Módulo 1: Home",
        "Módulo 2: Carga del dataset",
        "Módulo 3: Análisis Exploratorio de Datos (EDA)",
        "Módulo 4: Conclusiones finales",
    ],
)

# -------------------------------------------------------------------------
# MÓDULO 1: HOME (PRESENTACIÓN DEL PROYECTO)
# -------------------------------------------------------------------------
if opcion_menu == "Módulo 1: Home":
    st.title("📊 Análisis de Renovación de Pólizas de Seguro")
    st.caption("Caso de estudio aplicado como Producto Analítico Real")

    # Separación visual usando columnas para una interfaz ordenada
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.header("Contexto del Proyecto")
        st.write(
            """
        Este proyecto consiste en el desarrollo de una herramienta interactiva orientada al 
        **Análisis Exploratorio de Datos (EDA)** del dataset *InsuranceCompany.csv*. 
        El objetivo principal no es la construcción de modelos predictivos, sino aplicar 
        conceptos analíticos integrados para comprender a fondo los factores clave que influyen 
        en la decisión de renovación de una póliza de seguro, utilizando la variable `renewal` 
        como foco estratégico de negocio.
        """
        )

        st.subheader("Sobre el Dataset")
        st.write(
            """
        El conjunto de datos contiene información histórica integral de clientes de una compañía de seguros. 
        Incluye variables demográficas (edad, ingresos, tipo de residencia), historial detallado de pagos, 
        comportamiento de morosidad segmentado por ventanas temporales, canal de captación de clientes 
        y el puntaje de evaluación del nivel de riesgo.
        """
        )

        st.subheader("Tecnologías Utilizadas")
        st.markdown(
            """
        *   **Lenguaje Base:** Python
        *   **Interfaz Interactiva:** Streamlit (Sidebar, Tabs, Columns, Widgets)
        *   **Manipulación de Datos:** Pandas y NumPy
        *   **Visualización de Datos:** Matplotlib y Seaborn
        *   **Paradigma de Programación:** Programación Orientada a Objetos (POO)
        """
        )

    with col2:
        # Tarjeta informativa del Autor del Proyecto
        st.info("### Datos del Autor")
        st.markdown("**Nombre Completo:** [Tu Nombre y Apellido]")
        st.markdown("**Curso / Especialización:** Data Science / Analítica de Datos")
        st.markdown("**Año:** 2026")

        st.divider()
        st.success(
            "💡 **Instrucciones:** Usa el menú de la izquierda en la barra lateral para pasar al "
            "**Módulo 2** y cargar el archivo `.csv` para iniciar con la aplicación."
        )

# -------------------------------------------------------------------------
# ESPACIOS RESERVADOS PARA LOS SIGUIENTES MÓDULOS
# -------------------------------------------------------------------------
elif opcion_menu == "Módulo 2: Carga del dataset":
    st.title("📂 Módulo 2: Carga del dataset")
    st.write(
        "Sube el archivo de datos oficial para activar las herramientas de análisis de la aplicación."
    )

    # 1. Widget de carga obligatorio
    archivo_cargado = st.file_uploader(
        "Selecciona el archivo InsuranceCompany.csv", type=["csv"]
    )

    if archivo_cargado is not None:
        try:
            # 2. Carga del dataframe empleando Pandas
            # Guardamos el dataframe en el estado de la sesión (st.session_state)
            # para que persista y sea accesible desde el Módulo 3 de EDA.
            st.session_state["df_seguros"] = pd.read_csv(archivo_cargado)

            # Mensaje de validación exitosa
            st.success("¡Archivo cargado y validado correctamente!")

            # 3. Mostrar dimensiones usando st.columns
            df_actual = st.session_state["df_seguros"]
            filas, columnas = df_actual.shape

            col_filas, col_columnas = st.columns(2)
            with col_filas:
                st.metric(label="Número Total de Registros (Filas)", value=filas)
            with col_columnas:
                st.metric(label="Variables Registradas (Columnas)", value=columnas)

            st.divider()

            # 4. Vista previa de los datos (head)
            st.subheader("📋 Vista previa de los primeros registros (df.head())")
            st.dataframe(df_actual.head(10), use_container_width=True)

            st.info(
                "💡 **Siguiente paso:** Ahora que los datos están en memoria, puedes dirigirte al "
                "**Módulo 3: Análisis Exploratorio de Datos (EDA)** en la barra lateral."
            )

        except Exception as e:
            st.error(
                f"Error al procesar el archivo. Asegúrate de que sea un CSV válido. Detalle: {e}"
            )

    else:
        # Bloqueo visual preventivo si no hay archivo
        st.info("Por favor, arrastra o selecciona el archivo CSV para continuar.")
        st.warning(
            "⚠️ **Restricción de flujo:** Las herramientas del Módulo 3 y 4 permanecerán "
            "inactivas hasta que se complete la carga exitosa de este archivo."
        )


elif opcion_menu == "Módulo 3: Análisis Exploratorio de Datos (EDA)":
    st.title("📈 Módulo 3: Análisis Exploratorio de Datos (EDA)")
    st.warning(
        "Espacio reservado. Aquí se desplegarán las pestañas (tabs) con los 10 ítems de análisis."
    )

elif opcion_menu == "Módulo 4: Conclusiones finales":
    st.title("🎯 Módulo 4: Conclusiones finales")
    st.warning(
        "Espacio reservado. Aquí se estructurarán las 5 conclusiones de negocio."
    )
