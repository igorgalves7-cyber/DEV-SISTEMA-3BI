from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/produtos", tags=["Produtos"])


class ProdutoCreate(BaseModel):
    nome: str
    unidade: str
    quantidade_estoque: float = 0.0


class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    unidade: Optional[str] = None
    quantidade_estoque: Optional[float] = None


def buscar_produto(db: Session, id: int):
    produto = db.query(models.Produto).filter(models.Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()


@router.get("/{id}")
def obter(id: int, db: Session = Depends(get_db)):
    return buscar_produto(db, id)


@router.post("/", status_code=201)
def criar(dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto = models.Produto(**dados.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


@router.put("/{id}")
def atualizar(id: int, dados: ProdutoUpdate, db: Session = Depends(get_db)):
    produto = buscar_produto(db, id)
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(produto, campo, valor)
    db.commit()
    db.refresh(produto)
    return produto


@router.delete("/{id}")
def remover(id: int, db: Session = Depends(get_db)):
    produto = buscar_produto(db, id)
    db.delete(produto)
    db.commit()
    return {"mensagem": "Produto removido"}