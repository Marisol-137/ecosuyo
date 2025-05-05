import streamlit as st
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

st.set_page_config(page_title="Estadísticas", layout="wide")

st.title("📊 Estadísticas de los datos")

# Ruta donde se guardan los archivos
uploads_path = "data/uploads"

# Buscar el archivo más reciente
archivos = glob.glob(f"{uploads_path}/*.csv") + glob.glob(f"{uploads_path}/*.xls*")

if not archivos:
    st.warning("No hay archivos de datos disponibles. Por favor, sube uno desde la página de Datos.")
else:
    archivo_reciente = max(archivos, key=os.path.getmtime)
    st.success(f"Mostrando estadísticas del archivo: `{os.path.basename(archivo_reciente)}`")

    # Cargar el DataFrame
    try:
        if archivo_reciente.endswith(".csv"):
            df = pd.read_csv(archivo_reciente)
        else:
            df = pd.read_excel(archivo_reciente)
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        st.stop()

    # Mostrar resumen estadístico
    st.subheader("Resumen estadístico")
    st.dataframe(df.describe())

    # Selección de columna para graficar
    columnas_numericas = df.select_dtypes(include=["number"]).columns.tolist()
    if columnas_numericas:
        st.subheader("Gráfico de columnas numéricas")
        col = st.selectbox("Selecciona una columna para graficar:", columnas_numericas)
        tipo = st.radio("Tipo de gráfico", ["Barras", "Línea"])

        fig, ax = plt.subplots()
        if tipo == "Barras":
            ax.bar(df.index, df[col])
        else:
            ax.plot(df.index, df[col])

        ax.set_title(f"{tipo} - {col}")
        ax.set_xlabel("Índice")
        ax.set_ylabel(col)
        st.pyplot(fig)
    else:
        st.info("No hay columnas numéricas para graficar.")
