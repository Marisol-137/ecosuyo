import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from langchain_module.model_client import get_llm_response

load_dotenv()  # Carga las variables del .env

prompt = "¿Qué beneficios tiene el reciclaje del agua en la agricultura?"
respuesta = get_llm_response(prompt)
print("🧠 Respuesta del modelo:")
print(respuesta)
