from fastapi import FastAPI
from .routers import alunos, professores, aulas

app = FastAPI(title="Gestão de Aulas API - Refatorada")

app.include_router(alunos.router)
app.include_router(professores.router)
app.include_router(aulas.router)

@app.get("/")
def read_root():
    return {"message": "API de Gestão de Aulas está rodando! Acesse /docs para a documentação."}
