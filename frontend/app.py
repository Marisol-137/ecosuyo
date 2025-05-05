import streamlit as st
from pathlib import Path
import sys

# Agrega la carpeta 'pages' al path si no está
PAGES_DIR = Path(__file__).resolve().parent / "pages"
if str(PAGES_DIR) not in sys.path:
    sys.path.append(str(PAGES_DIR))

# Importa los módulos desde la carpeta pages
import pagina_datos as datos
import pagina_estadisticas as estadisticas
import analisis_chat as chat

# Carga de estilos CSS
st.set_page_config(page_title="Ecosuyo", layout="wide")

with open("frontend/style/custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar con logo y navegación
st.sidebar.image("frontend/assets/logo.png", use_container_width=True)
st.sidebar.markdown("## Ecosuyo")
pagina = st.sidebar.radio("Ir a:", [
    "📥 Ingreso de datos",
    "📊 Estadísticas",
    "💬 Análisis y Chat"
])

# Renderizado condicional según opción
if pagina == "📥 Ingreso de datos":
    datos.mostrar()
elif pagina == "📊 Estadísticas":
    estadisticas.mostrar()
elif pagina == "💬 Análisis y Chat":
    chat.mostrar()
