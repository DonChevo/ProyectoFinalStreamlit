import pandas as pd
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
    
    # CONTROL DE FLUJO: Validar que el archivo exista en memoria
    if "df_seguros" not in st.session_state:
        st.warning("⚠️ **Acceso denegado:** No se ha detectado ningún dataset en memoria.")
        st.info("Por favor, dirígete al **Módulo 2: Carga del dataset** en la barra lateral y sube el archivo CSV.")
    else:
        # Importación local de la clase para evitar dependencias circulares
        from src.analyzer import DataProcessor
        
        # Instanciar la clase POO con el DataFrame almacenado en sesión
        df_activo = st.session_state["df_seguros"]
        procesador = DataProcessor(df_activo)
        
        st.write("Explora las métricas fundamentales, distribución de variables y calidad de los datos cargados.")
        
        # Creación de pestañas para los primeros 4 ítems solicitados        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "Ítem 1: Info General", 
            "Ítem 2: Clasificación", 
            "Ítem 3: Descriptivos", 
            "Ítem 4: Valores Faltantes",
            "Ítem 5: Distribución Numérica",
            "Ítem 6: Análisis Categórico"
        ])

        
        # --- ÍTEM 1: INFORMACIÓN GENERAL ---
        with tab1:
            st.header("📋 Información General del Dataset")
            st.write("Muestra un resumen técnico de los tipos de datos mapeados y la completitud del archivo.")
            
            info_general = procesador.obtener_info_general()
            st.dataframe(info_general, use_container_width=True)
            
        # --- ÍTEM 2: CLASIFICACIÓN DE VARIABLES ---
        with tab2:
            st.header("🗂️ Clasificación Automática de Variables")
            st.write("Identificación y conteo de tipos de datos estadísticos mediante una función personalizada (POO).")
            
            resultado_clase = procesador.clasificar_variables()
            
            col_num, col_cat = st.columns(2)
            with col_num:
                st.metric(label="Variables Numéricas Detectadas", value=resultado_clase["numéricas"]["conteo"])
                st.write("**Columnas:**", resultado_clase["numéricas"]["lista"])
            with col_cat:
                st.metric(label="Variables Categóricas Detectadas", value=resultado_clase["categóricas"]["conteo"])
                st.write("**Columnas:**", resultado_clase["categóricas"]["lista"])
                
        # --- ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS ---
        with tab3:
            st.header("📊 Resumen de Estadísticas Descriptivas")
            st.write("Análisis de tendencias centrales, dispersión y frecuencias globales de las variables de seguros.")
            
            descriptivos = procesador.obtener_descriptivos()
            # Mostramos un dataframe con barra de scroll horizontal para fácil lectura
            st.dataframe(descriptivos, use_container_width=True)
            
            st.markdown("""
            **Interpretación básica preliminar:**
            *   Revisa la fila `mean` (media) y `50%` (mediana) en las columnas numéricas para evaluar asimetrías.
            *   Las filas `unique`, `top` y `freq` te darán los primeros indicios del comportamiento de tus variables categóricas.
            """)
            
        # --- ÍTEM 4: ANÁLISIS DE VALORES FALTANTES ---
        with tab4:
            st.header("🔍 Análisis de Valores Faltantes (Nulos)")
            st.write("Evaluación cuantitativa y visual de vacíos de información en el histórico de clientes.")
            
            resumen_nulos, figura_nulos = procesador.analizar_valores_faltantes()
            
            col_tabla, col_grafico = st.columns([1, 2])
            with col_tabla:
                st.write("**Tabla de Frecuencias de Nulos:**")
                st.dataframe(resumen_nulos, use_container_width=True)
            with col_grafico:
                st.write("**Visualización de la distribución de vacíos:**")
                st.pyplot(figura_nulos)
                
            st.caption("Discusión breve: Es fundamental identificar variables con alta concentración de nulos antes de realizar cruces bivariados.")

                # --- ÍTEM 5: DISTRIBUCIÓN DE VARIABLES NUMÉRICAS ---
        with tab5:
            st.header("📊 Distribución de Variables Numéricas")
            st.write("Visualiza la forma, dispersión y simetría de los datos numéricos mediante histogramas dinámicos.")
            
            # Extraemos la lista de numéricas calculada dinámicamente en el Ítem 2
            lista_numericas = resultado_clase["numéricas"]["lista"]
            
            # Selector interactivo para el usuario
            var_num_seleccionada = st.selectbox(
                "Selecciona la variable numérica a analizar:", 
                options=lista_numericas,
                key="sb_item5"
            )
            
            # Generar y mostrar el gráfico desde el backend
            fig_dist = procesador.graficar_distribucion_numerica(var_num_seleccionada)
            st.pyplot(fig_dist)
            
            st.markdown("""
            **Guía de interpretación visual:**
            *   Si la **Media (línea roja)** está muy separada de la **Mediana (línea verde)**, la variable presenta asimetría (sesgo).
            *   La curva de densidad (KDE) te ayuda a ver si los datos se concentran en un único punto o forman múltiples picos.
            """)

        # --- ÍTEM 6: ANÁLISIS DE VARIABLES CATEGÓRICAS ---
        with tab6:
            st.header("🗂️ Análisis de Variables Categóricas")
            st.write("Revisa la frecuencia y proporción de clientes dentro de cada segmento del negocio.")
            
            # Extraemos la lista de categóricas calculada dinámicamente en el Ítem 2
            lista_categoricas = resultado_clase["categóricas"]["lista"]
            
            # Selector interactivo para el usuario
            var_cat_seleccionada = st.selectbox(
                "Selecciona la variable categórica a analizar:", 
                options=lista_categoricas,
                key="sb_item6"
            )
            
            # Llamada al método que procesa la tabla de frecuencias y la figura
            df_frecuencias, fig_cat = procesador.analizar_variable_categorica(var_cat_seleccionada)
            
            col_tab6_tabla, col_tab6_graf = st.columns(2)
            with col_tab6_tabla:
                st.write("**Tabla de Frecuencias e Impacto Relativo:**")
                st.dataframe(df_frecuencias, use_container_width=True)
            with col_tab6_graf:
                st.write("**Composición Visual (Gráfico de Barras):**")
                st.pyplot(fig_cat)


elif opcion_menu == "Módulo 4: Conclusiones finales":
    st.title("🎯 Módulo 4: Conclusiones finales")
    st.warning(
        "Espacio reservado. Aquí se estructurarán las 5 conclusiones de negocio."
    )
