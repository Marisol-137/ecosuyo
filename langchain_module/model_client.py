import pandas as pd
from langchain_community.llms import WatsonxLLM
import os

def get_llm():
    return WatsonxLLM(
        model_id=os.getenv("WATSONX_MODEL_ID", "ibm/granite-13b-instruct-v2"),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        credentials={
            "apikey": os.getenv("WATSONX_API_KEY"),
            "url": os.getenv("WATSONX_URL")
        }
    )

def cargar_prompt(path="langchain_module/prompt_templates/chat_prompt.txt") -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def cargar_contexto_crudo():
    contexto = ""
    rutas = [
        "data/uploads/ingresos_ropa_10_dias.csv",
        "data/uploads/egresos_ropa_10_dias.csv"
    ]
    for ruta in rutas:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta)
            contexto += f"Contenido de {os.path.basename(ruta)}:\n{df.to_string(index=False)}\n\n"
    return contexto.strip()

def get_llm_response(question: str) -> str:
    llm = get_llm()
    prompt_template = cargar_prompt()
    context = cargar_contexto_crudo()
    prompt_final = prompt_template.format(context=context, question=question)
    return llm.invoke(prompt_final)
