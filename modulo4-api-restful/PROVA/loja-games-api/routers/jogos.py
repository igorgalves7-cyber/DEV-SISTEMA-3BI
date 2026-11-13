from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Jogo, Plataforma, Avaliacao

router = APIRouter(prefix="/jogos", tags=["Jogos"])


class JogoCreate(BaseModel):
    titulo: str
    genero: str
    preco: float
    plataforma_id: int


@router.get("/")
def listar_jogos(db: Session = Depends(get_db)):
    return db.query(Jogo).all()


@router.get("/{id}")
def buscar_jogo(id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(404, "Jogo não encontrado")

    return jogo


@router.post("/")
def cadastrar_jogo(jogo: JogoCreate, db: Session = Depends(get_db)):
    plataforma = db.query(Plataforma).filter(
        Plataforma.id == jogo.plataforma_id
    ).first()

    if not plataforma:
        raise HTTPException(404, "Plataforma não encontrada")

    novo = Jogo(**jogo.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


@router.put("/{id}")
def atualizar_jogo(id: int, dados: JogoCreate, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(404, "Jogo não encontrado")

    plataforma = db.query(Plataforma).filter(
        Plataforma.id == dados.plataforma_id
    ).first()

    if not plataforma:
        raise HTTPException(404, "Plataforma não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(jogo, campo, valor)

    db.commit()
    db.refresh(jogo)

    return jogo


@router.delete("/{id}")
def remover_jogo(id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(404, "Jogo não encontrado")

    db.delete(jogo)
    db.commit()

    return {"mensagem": "Jogo removido com sucesso"}


@router.get("/{id}/avaliacoes")
def listar_avaliacoes(id: int, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(404, "Jogo não encontrado")

    return db.query(Avaliacao).filter(Avaliacao.jogo_id == id).all()