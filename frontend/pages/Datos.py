import streamlit as st
import pandas as pd
import os

def mostrar():
    st.markdown("## Ingreso de datos")
    st.markdown("Aquí puedes subir tus archivos o grabar audio para ingresar datos.")

    archivo = st.file_uploader("Sube un archivo CSV, Excel o audio (.wav, .mp3)", type=["csv", "xlsx", "xls", "wav", "mp3"])

    if archivo is not None:
        nombre_archivo = archivo.name
        ruta_destino = os.path.join("data", "uploads", nombre_archivo)

        with open(ruta_destino, "wb") as f:
            f.write(archivo.getbuffer())

        st.success(f"Archivo guardado en: `{ruta_destino}`")

        if nombre_archivo.endswith((".csv", ".xlsx", ".xls")):
            try:
                if nombre_archivo.endswith(".csv"):
                    df = pd.read_csv(ruta_destino)
                else:
                    df = pd.read_excel(ruta_destino)
                st.markdown("### Vista previa de los datos:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"No se pudo cargar el archivo: {e}")
        elif nombre_archivo.endswith((".wav", ".mp3")):
            st.audio(ruta_destino)
            st.markdown("✅ Audio subido correctamente.")

# Esta línea es crucial para que se ejecute al abrirse la página
mostrar()
