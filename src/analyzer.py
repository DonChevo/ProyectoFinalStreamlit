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

    def obtener_info_general(self) -> dict:
        """Ítem 1: Obtiene información general sobre tipos de datos y nulos."""
        info = {
            "dimensiones": self.df.shape,
            "tipos_datos": self.df.dtypes,
            "valores_nulos": self.df.isnull().sum(),
        }
        return info

    def clasificar_variables(self) -> tuple:
        """Ítem 2: Clasifica de forma automática las variables en numéricas y

        categóricas.

        :return: Tupla con (lista_numericas, lista_categoricas)
        """
        # Excluimos el 'id' por ser un identificador único sin valor estadístico
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

        return numericas, categoricas

    def obtener_descriptivos(self) -> pd.DataFrame:
        """Ítem 3: Retorna las estadísticas descriptivas básicas de las

        variables.
        """
        return self.df.describe(include="all")

    # Los métodos para gráficos generarán figuras de matplotlib/seaborn
    # para ser renderizadas dinámicamente en app.py mediante st.pyplot()
