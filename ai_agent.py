from langchain_module.model_client import get_llm_response
from backend.services.stats_engine import generar_contexto_descriptivo

def responder_con_contexto(pregunta, ruta_csv):
    contexto = generar_contexto_descriptivo(ruta_csv)
    prompt = f"{contexto}\n\nPregunta del usuario: {pregunta}"
    respuesta = get_llm_response(prompt)
    return respuesta
