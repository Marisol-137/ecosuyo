import pandas as pd

def generar_contexto_descriptivo(path_csv):
    df = pd.read_csv(path_csv)
    resumen = df.describe(include='all').to_string()
    columnas = ", ".join(df.columns)
    contexto = f"""Este es un resumen estadístico del archivo {path_csv}:\n\nColumnas: {columnas}\n\nResumen estadístico:\n{resumen}"""
    return contexto
