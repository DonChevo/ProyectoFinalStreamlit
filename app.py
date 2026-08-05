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
        "1: Home",
        "2: Carga del dataset",
        "3: EDA",
        "4: Conclusiones",
    ],
)

# -------------------------------------------------------------------------
# MÓDULO 1: HOME (PRESENTACIÓN DEL PROYECTO)
# -------------------------------------------------------------------------
if opcion_menu == "1: Home":
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
        st.markdown("**Nombre Completo:** JULIO CESAR RODRIGUEZ RODRIGUEZ")
        st.markdown("**Curso:** Especialización en Python Analytics")
        st.markdown("**Año:** 2026")

        st.divider()
        st.success(
            "💡 **Instrucciones:** Usa el menú de la izquierda en la barra lateral para pasar al "
            "**Módulo 2** y cargar el archivo `.csv` para iniciar con la aplicación."
        )

# -------------------------------------------------------------------------
# ESPACIOS RESERVADOS PARA LOS SIGUIENTES MÓDULOS
# -------------------------------------------------------------------------
elif opcion_menu == "2: Carga del dataset":
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


elif opcion_menu == "3: EDA":
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
        
        # Creación de pestañas para los 10 ítems obligatorios del EDA
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
            "Ítem 1: Info General", 
            "Ítem 2: Clasificación", 
            "Ítem 3: Descriptivos", 
            "Ítem 4: Valores Faltantes",
            "Ítem 5: Distribución Numérica",
            "Ítem 6: Análisis Categórico",
            "Ítem 7: Bivariado (Num vs Cat)",
            "Ítem 8: Bivariado (Cat vs Cat)",
            "Ítem 9: Análisis Parámetrico",
            "Ítem 10: Hallazgos Clave"
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
        
        # --- ÍTEM 7: ANÁLISIS BIVARIADO (NUMÉRICO VS CATEGÓRICO) ---
        with tab7:
            st.header("🔄 Análisis Bivariado: Métricas vs Renovación")
            st.write("Compara el comportamiento y los promedios de una variable numérica entre los clientes que renovaron y los que no.")
            
            # Recuperamos las variables numéricas, excluyendo 'id' si fuera necesario
            lista_numericas = resultado_clase["numéricas"]["lista"]
            
            var_biv_num = st.selectbox(
                "Selecciona la variable numérica para contrastar con 'renewal':",
                options=lista_numericas,
                key="sb_item7"
            )
            
            # Llamamos al backend (POO)
            tabla_medias, fig_biv_num = procesador.analizar_bivariado_num_cat(var_biv_num)
            
            col_t7_tabla, col_t7_graf = st.columns(2)
            with col_t7_tabla:
                st.write("**Comparativa de Medias Aritméticas:**")
                st.dataframe(tabla_medias, use_container_width=True)
                st.markdown("""
                **Tips de análisis:**
                * Revisa si el promedio de la variable cambia significativamente entre los grupos 'Yes' y 'No'.
                * Las diferencias en las cajas del gráfico indican si la métrica influye en la renovación.
                """)
            with col_t7_graf:
                st.write("**Distribución por Grupos (Boxplot):**")
                st.pyplot(fig_biv_num)

        # --- ÍTEM 8: ANÁLISIS BIVARIADO (CATEGÓRICO VS CATEGÓRICO) ---
        with tab8:
            st.header("🔄 Análisis Bivariado: Segmentos vs Renovación")
            st.write("Calcula la tasa de renovación porcentual según los diferentes perfiles o atributos categóricos de los clientes.")
            
            # Recuperamos las variables categóricas. Excluimos 'renewal' para no cruzarla consigo misma
            lista_categoricas = [c for c in resultado_clase["categóricas"]["lista"] if c != "renewal"]
            
            var_biv_cat = st.selectbox(
                "Selecciona la variable categórica para analizar su tasa de renovación:",
                options=lista_categoricas,
                key="sb_item8"
            )
            
            # Llamamos al backend (POO)
            tabla_contingencia, fig_biv_cat = procesador.analizar_bivariado_cat_cat(var_biv_cat)
            
            col_t8_tabla, col_t8_graf = st.columns(2)
            with col_t8_tabla:
                st.write("**Tabla de Contingencia y Tasas de Éxito:**")
                st.dataframe(tabla_contingencia, use_container_width=True)
            with col_t8_graf:
                st.write("**Estructura Proporcional (Barras Apiladas 100%):**")
                st.pyplot(fig_biv_cat)

        # --- ÍTEM 9: ANÁLISIS BASADO EN PARAMETROS SELECCIONADOS ---
        with tab9:
            st.header("🎛️ Análisis Paramétrico Dinámico")
            st.write("Selecciona múltiples variables numéricas para calcular su nivel de asociación lineal mediante el coeficiente de Pearson.")
            
            # Recuperamos las variables numéricas para el multiselect
            lista_numericas = resultado_clase["numéricas"]["lista"]
            
            # Widget multiselect interactivo
            vars_parametros = st.multiselect(
                "Selecciona las variables para la matriz de correlación:",
                options=lista_numericas,
                default=lista_numericas[:3] if len(lista_numericas) >= 3 else lista_numericas,
                key="ms_item9"
            )
            
            # Llamada al backend
            matriz_corr, fig_heatmap = procesador.analizar_parametrico_dinamico(vars_parametros)
            
            if not matriz_corr.empty:
                col_t9_tabla, col_t9_graf = st.columns(2)
                with col_t9_tabla:
                    st.write("**Matriz Numérica de Correlación:**")
                    st.dataframe(matriz_corr.round(2), use_container_width=True)
                    st.markdown("""
                    **Regla de lectura rápida:**
                    * Valores cercanos a **1.0** indican una correlación positiva fuerte.
                    * Valores cercanos a **-1.0** indican una correlación inversa fuerte.
                    * Valores cercanos a **0.0** indican ausencia de relación lineal.
                    """)
                with col_t9_graf:
                    st.write("**Mapa de Calor Visual (Heatmap):**")
                    st.pyplot(fig_heatmap)

        # --- ÍTEM 10: HALLAZGOS CLAVE ---
        with tab10:
            st.header("🎯 Hallazgos Clave e Insights Estratégicos")
            st.write("Visualización resumen diseñada para identificar patrones críticos de comportamiento de los clientes.")
            
            # Llamada al método de insights del backend
            df_insights, fig_scatter = procesador.generar_hallazgos_clave()
            
            col_t10_tabla, col_t10_graf = st.columns(2)
            with col_t10_tabla:
                st.write("**Métricas Promedio por Estado de Póliza:**")
                st.dataframe(df_insights, use_container_width=True)
                st.markdown("""
                **Interpretación del Negocio:**
                *   Analiza si los clientes con mayores **ingresos promedio** muestran una mayor tasa de renovación.
                *   Evalúa el impacto de los **pagos tardíos**: la morosidad recurrente suele ser el principal detonante de pólizas caídas.
                """)
            with col_t10_graf:
                st.write("**Mapa de Dispersión Comercial:**")
                st.pyplot(fig_scatter)


elif opcion_menu == "4: Conclusiones":
    st.title("🎯 Módulo 4: Conclusiones Finales y Recomendaciones")
    st.caption("Insights estratégicos derivados del Análisis Exploratorio de Datos (EDA) para la toma de decisiones de negocio.")

    # CONTROL DE FLUJO: Validar que el archivo exista en memoria para mantener consistencia
    if "df_seguros" not in st.session_state:
        st.warning("⚠️ **Acceso denegado:** No se ha detectado ningún dataset en memoria.")
        st.info("Por favor, dirígete al **Módulo 2: Carga del dataset** en la barra lateral, sube el archivo CSV y realiza el análisis para activar esta sección.")
    else:
        st.write(
            "A continuación se presentan las 5 conclusiones estratégicas fundamentadas en el comportamiento "
            "histórico de la cartera de clientes de la compañía de seguros:"
        )
        
        st.divider()

        # Estructura limpia usando contenedores visuales para legibilidad
        st.info("### 1. Impacto Crítico de la Morosidad Recurrente")
        st.write(
            "El análisis bivariado revela que los clientes con presencia de pagos tardíos, especialmente en la ventana "
            "de **3 a 6 meses de retraso**, presentan la tasa de caída de pólizas más agresiva del portafolio. "
            "La morosidad temprana es el indicador de alerta (red flag) más confiable para anticipar la no renovación."
        )

        st.info("### 2. Estabilidad Financiera e Ingreso Mensual")
        st.write(
            "Existe una relación positiva directa entre el **ingreso mensual (Income)** del asegurado y la renovación. "
            "Los segmentos de ingresos medio-altos exhiben una lealtad superior, sugiriendo que la pérdida de clientes en "
            "estratos de menores ingresos responde a barreras de asequibilidad económica ante la prima actual."
        )

        st.info("### 3. El Factor de Fidelización: Primas Históricas Pagadas")
        st.write(
            "Los clientes que registran un mayor **número total de primas pagadas históricamente** muestran una inercia de "
            "renovación significativamente alta. Esto demuestra que los asegurados que superan los ciclos iniciales críticos "
            "tienden a consolidarse en la compañía, validando el valor de las estrategias de retención temprana."
        )

        st.info("### 4. Eficiencia de los Canales de Captación")
        st.write(
            "El cruce bivariado categórico demostró disparidades notables en el rendimiento según el **sourcing_channel**. "
            "Ciertos canales de captación atraen clientes con perfiles de riesgo más estables y mejores puntajes de evaluación, "
            "mientras que otros sufren de altas tasas de deserción inmediata, lo que exige reevaluar las comisiones de adquisición."
        )

        st.info("### 5. Relevancia del Scoring de Suscripción")
        st.write(
            "La métrica **application_underwriting_score** probó ser un pilar fundamental de diagnóstico. Los clientes con "
            "puntuaciones robustas en la evaluación de riesgo inicial no solo presentan menor morosidad, sino que mantienen "
            "un comportamiento de renovación homogéneo, justificando un enfoque de incentivos o descuentos para este grupo selecto."
        )

        st.divider()
        
        # Cuadro de cierre metodológico
        st.success(
            "💡 **Nota del Desarrollador:** Estas conclusiones cumplen con el enfoque del entregable: "
            "están orientadas puramente al entendimiento del estado actual del negocio y soporte de decisiones estratégicas, "
            "evitando sesgos o metodologías predictivas avanzadas fuera del alcance del módulo."
        )

