import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class DataProcessor:
    """Clase encargada de encapsular la lógica del Análisis Exploratorio de

    Datos (EDA) y procesamiento del dataset de seguros.
    """

    def __init__(self, df: pd.DataFrame):
        """Inicializa la clase con el DataFrame cargado.

        :param df: DataFrame de Pandas con los datos de InsuranceCompany.csv
        """
        self.df = df

    def obtener_info_general(self) -> pd.DataFrame:
        """Ítem 1: Información general del dataset.

        Simula el comportamiento de .info() construyendo un resumen tabular
        con los tipos de datos y recuento de valores no nulos.
        """
        info_df = pd.DataFrame(
            {
                "Tipo de Dato": self.df.dtypes.astype(str),
                "Valores No Nulos": self.df.notnull().sum(),
                "Valores Nulos": self.df.isnull().sum(),
            }
        )
        return info_df

    def clasificar_variables(self) -> dict:
        """Ítem 2: Clasificación de variables.

        Usa una función personalizada bajo POO para identificar columnas
        numéricas y categóricas, excluyendo el 'id'.
        """
        columnas_analisis = [col for col in self.df.columns if col != "id"]

        numericas = (
            self.df[columnas_analisis]
            .select_dtypes(include=[np.number])
            .columns.tolist()
        )
        categoricas = (
            self.df[columnas_analisis]
            .select_dtypes(include=["object", "category"])
            .columns.tolist()
        )

        return {
            "numéricas": {
                "lista": numericas,
                "conteo": len(numericas),
            },
            "categóricas": {
                "lista": categoricas,
                "conteo": len(categoricas),
            },
        }

    def obtener_descriptivos(self) -> pd.DataFrame:
        """Ítem 3: Estadísticas descriptivas.

        Retorna un resumen de estadística descriptiva (.describe()) tanto para
        variables numéricas como categóricas si están presentes.
        """
        return self.df.describe(include="all")

    def analizar_valores_faltantes(self):
        """Ítem 4: Análisis de valores faltantes (Conteo y Gráfico).

        Calcula las frecuencias absolutas y relativas de valores nulos, y
        genera un objeto Figure de Matplotlib para graficar su presencia.
        """
        totales = self.df.isnull().sum()
        porcentajes = (self.df.isnull().sum() / len(self.df)) * 100

        resumen_nulos = pd.DataFrame(
            {"Total Nulos": totales, "Porcentaje (%)": porcentajes.round(2)}
        ).sort_values(by="Total Nulos", ascending=False)

        # Generar gráfico solo para las columnas que tienen nulos
        columnas_con_nulos = totales[totales > 0]

        fig, ax = plt.subplots(figsize=(8, 4))
        if not columnas_con_nulos.empty:
            sns.barplot(
                x=columnas_con_nulos.values,
                y=columnas_con_nulos.index,
                palette="Reds_r",
                ax=ax,
            )
            ax.set_title("Cantidad de Valores Faltantes por Variable")
            ax.set_xlabel("Número de registros nulos")
        else:
            # Si no hay nulos, se genera un gráfico limpio con texto indicativo
            ax.text(
                0.5,
                0.5,
                "No se detectaron valores faltantes\nen este dataset.",
                color="green",
                fontsize=14,
                ha="center",
                va="center",
            )
            ax.axis("off")

        return resumen_nulos, fig
    
    def graficar_distribucion_numerica(self, columna: str):
        """Ítem 5: Distribución de variables numéricas.

        Genera un histograma con una línea de densidad estimada (KDE) para
        analizar la forma de la distribución de la variable seleccionada.
        """
        fig, ax = plt.subplots(figsize=(8, 4))

        # Creamos el histograma usando Seaborn
        sns.histplot(
            data=self.df, x=columna, kde=True, color="#1f77b4", bins=30, ax=ax
        )

        ax.set_title(f"Distribución de la Variable: {columna}", fontsize=12)
        ax.set_xlabel(columna)
        ax.set_ylabel("Frecuencia (Conteo)")

        # Estadísticos guía para la interpretación visual
        media = self.df[columna].mean()
        mediana = self.df[columna].median()
        ax.axvline(
            media,
            color="red",
            linestyle="--",
            label=f"Media: {media:,.2f}",
        )
        ax.axvline(
            mediana,
            color="green",
            linestyle="-.",
            label=f"Mediana: {mediana:,.2f}",
        )
        ax.legend()

        return fig

    def analizar_variable_categorica(self, columna: str) -> tuple:
        """Ítem 6: Análisis de variables categóricas.

        Calcula el conteo de frecuencias absolutas y relativas, y genera un
        gráfico de barras horizontales para la variable elegida.
        """
        # 1. Cálculo de frecuencias y proporciones
        conteo = self.df[columna].value_counts()
        proporcion = self.df[columna].value_counts(normalize=True) * 100

        df_frecuencias = pd.DataFrame(
            {"Conteo Absoluto": conteo, "Proporción (%)": proporcion.round(2)}
        )

        # 2. Generación del gráfico de barras
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(
            x=conteo.values, y=conteo.index.astype(str), palette="Blues_r", ax=ax
        )

        ax.set_title(f"Análisis de Frecuencias: {columna}", fontsize=12)
        ax.set_xlabel("Cantidad de Clientes")
        ax.set_ylabel(columna)

        return df_frecuencias, fig

    def analizar_bivariado_num_cat(self, columna_num: str):
        """
        Ítem 7: Análisis bivariado (Numérico vs Categórico).
        Compara cómo se comporta una variable numérica seleccionada según
        si el cliente renovó o no su póliza ('renewal'), usando un Boxplot.
        """
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Clonamos temporalmente la columna convirtiéndola a String (texto)
        # Esto soluciona el error si los datos vienen mapeados como 0 y 1 enteros.
        df_temporal = self.df.copy()
        df_temporal['renewal_txt'] = df_temporal['renewal'].astype(str)

        # Creamos el gráfico de caja (Boxplot) apuntando a la nueva columna de texto
        sns.boxplot(
            data=df_temporal, 
            x="renewal_txt", 
            y=columna_num, 
            palette="Set2", 
            ax=ax
        )

        ax.set_title(f"Análisis de {columna_num} segmentado por Renovación (renewal)", fontsize=12)
        ax.set_xlabel("¿Renovó la Póliza? (renewal)")
        ax.set_ylabel(columna_num)

        # Calculamos la media de cada grupo de forma segura usando la columna de texto
        resumen_medias = df_temporal.groupby("renewal_txt")[columna_num].mean().to_frame()
        resumen_medias.columns = [f"Media de {columna_num}"]

        return resumen_medias, fig

    def analizar_bivariado_cat_cat(self, columna_cat: str):
        """
        Ítem 8: Análisis bivariado (Categórico vs Categórico).
        Cruza una variable categórica seleccionada con la variable 'renewal'
        para calcular tasas de renovación mediante una tabla de contingencia.
        """
        # Clonamos temporalmente para asegurar que la columna objetivo sea texto limpio
        df_temporal = self.df.copy()
        df_temporal['renewal_txt'] = df_temporal['renewal'].astype(str)

        # 1. Tabla de contingencia cruzada (Frecuencias absolutas)
        tabla_cruzada = pd.crosstab(df_temporal[columna_cat], df_temporal["renewal_txt"])

        # 2. Calcular porcentajes por fila para ver la tasa de renovación por segmento
        tabla_porcentajes = pd.crosstab(
            df_temporal[columna_cat], 
            df_temporal["renewal_txt"], 
            normalize="index"
        ) * 100

        # Identificación dinámica de columnas para evitar buscar textos fijos
        # Ordenamos las columnas del crosstab para tener consistencia visual
        columnas_existentes = sorted(tabla_cruzada.columns.tolist())
        
        # Asignamos de forma segura las series según la posición encontrada
        col_no = columnas_existentes[0] if len(columnas_existentes) > 0 else None
        col_yes = columnas_existentes[1] if len(columnas_existentes) > 1 else None

        # 3. Construcción segura del DataFrame de reporte final
        reporte_bivariado = pd.DataFrame(index=tabla_cruzada.index)
        
        if col_no is not None:
            reporte_bivariado["No Renovó (Cant.)"] = tabla_cruzada[col_no]
            reporte_bivariado["Tasa No Renovación (%)"] = tabla_porcentajes[col_no].round(2)
        else:
            reporte_bivariado["No Renovó (Cant.)"] = 0
            reporte_bivariado["Tasa No Renovación (%)"] = 0.0

        if col_yes is not None:
            reporte_bivariado["Renovó (Cant.)"] = tabla_cruzada[col_yes]
            reporte_bivariado["Tasa Renovación (%)"] = tabla_porcentajes[col_yes].round(2)
        else:
            reporte_bivariado["Renovó (Cant.)"] = 0
            reporte_bivariado["Tasa Renovación (%)"] = 0.0

        # 4. Gráfico de barras apiladas (Stacked Bar Chart) al 100%
        fig, ax = plt.subplots(figsize=(8, 4))
        tabla_porcentajes.plot(kind="bar", stacked=True, color=["#e74c3c", "#2ecc71"], ax=ax)

        ax.set_title(f"Proporción de Renovación según {columna_cat}", fontsize=12)
        ax.set_xlabel(columna_cat)
        ax.set_ylabel("Porcentaje (%)")
        ax.legend(title="¿Renovó?", labels=["Grupo 0 / No", "Grupo 1 / Yes"][:len(columnas_existentes)])
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        return reporte_bivariado, fig

    def analizar_parametrico_dinamico(self, columnas_seleccionadas: list):
        """
        Ítem 9: Análisis basado en parámetros seleccionados.
        Calcula una matriz de correlación de Pearson únicamente para las variables
        numéricas elegidas por el usuario y genera un mapa de calor (Heatmap).
        """
        if len(columnas_seleccionadas) < 2:
            # Si el usuario elige menos de 2 variables, generamos una figura vacía con un aviso
            fig, ax = plt.subplots(figsize=(6, 3))
            ax.text(0.5, 0.5, "Por favor, selecciona al menos 2 variables\npara calcular la matriz de correlación.", 
                    color="orange", fontsize=11, ha="center", va="center")
            ax.axis("off")
            return pd.DataFrame(), fig

        # 1. Calcular matriz de correlación
        matriz_corr = self.df[columnas_seleccionadas].corr(method="pearson")

        # 2. Generar Mapa de Calor (Heatmap)
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(
            matriz_corr, 
            annot=True, 
            cmap="Coolwarm", 
            fmt=".2f", 
            vmin=-1, 
            vmax=1, 
            linewidths=0.5, 
            ax=ax
        )
        ax.set_title("Matriz de Correlación Paramétrica Dinámica", fontsize=12)
        plt.tight_layout()

        return matriz_corr, fig

    def generar_hallazgos_clave(self) -> tuple:
        """
        Ítem 10: Hallazgos clave e Insights principales.
        Genera un análisis estratégico cruzando los ingresos (Income) con el historial 
        de morosidad (Count_3-6_months_late) segmentado por la renovación.
        """
        # Identificamos variables clave para el negocio: ingresos promedio según renovación
        df_temporal = self.df.copy()
        df_temporal['renewal_txt'] = df_temporal['renewal'].astype(str)
        
        reporte_insight = df_temporal.groupby('renewal_txt').agg({
            'Income': 'mean',
            'Count_3-6_months_late': 'mean',
            'no_of_premiums_paid': 'mean'
        }).round(2)
        
        reporte_insight.columns = ["Ingreso Promedio", "Promedio Pagos Tardíos (3-6m)", "Total Primas Pagadas"]

        # Gráfico estratégico: Relación entre Ingresos y Primas Pagadas por el cliente
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(
            data=df_temporal,
            x="no_of_premiums_paid",
            y="Income",
            hue="renewal_txt",
            palette={"1.0": "#2ecc71", "0.0": "#e74c3c", "1": "#2ecc71", "0": "#e74c3c", "Yes": "#2ecc71", "No": "#e74c3c"},
            alpha=0.6,
            ax=ax
        )
        ax.set_title("Mapa Estratégico: Primas Pagadas vs Ingreso Mensual", fontsize=12)
        ax.set_xlabel("Número de Primas Pagadas")
        ax.set_ylabel("Ingresos Mensuales")
        ax.legend(title="¿Renovó?")
        plt.tight_layout()

        return reporte_insight, fig
