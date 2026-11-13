from fastapi import FastAPI
from database import Base, engine
from routers import plataformas, jogos, avaliacoes
from tags import tags_metadata

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Loja de Games API",
    description="API para gerenciamento de plataformas, jogos e avaliações.",
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)


@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo à API da Loja de Games!"}