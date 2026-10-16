from fastapi import FastAPI

import models  # noqa: F401  (garante o registro do modelo antes do create_all)
from database import Base, engine
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Livros API", version="1.0.0")
app.include_router(router)


@app.get("/", tags=["Raiz"])
def raiz():
    return {"mensagem": "Livros API no ar. Documentação em /docs"}