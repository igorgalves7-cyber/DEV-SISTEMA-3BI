from fastapi import FastAPI
from database import engine, Base
import models
from routers import usuarios, produtos, movimentacoes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Almoxarifado")

app.include_router(usuarios.router)
app.include_router(produtos.router)
app.include_router(movimentacoes.router)