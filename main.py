from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


# Caminho do arquivo HTML
caminho = "lista_musica.html"

# Lê o conteúdo do arquivo como texto
with open(caminho, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():    

    html = f"""{conteudo}"""

    return HTMLResponse(html)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
