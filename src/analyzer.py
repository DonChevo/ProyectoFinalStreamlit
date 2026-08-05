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

