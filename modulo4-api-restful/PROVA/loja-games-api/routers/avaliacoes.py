from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import get_db
from models import Avaliacao, Jogo

router = APIRouter(prefix="/avaliacoes", tags=["Avaliações"])


class AvaliacaoCreate(BaseModel):
    nota: int = Field(..., ge=1, le=5)
    comentario: str
    jogo_id: int


@router.post("/")
def registrar_avaliacao(
    avaliacao: AvaliacaoCreate,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(
        Jogo.id == avaliacao.jogo_id
    ).first()

    if not jogo:
        raise HTTPException(404, "Jogo não encontrado")

    nova = Avaliacao(**avaliacao.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)

    return nova


@router.delete("/{id}")
def remover_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao = db.query(Avaliacao).filter(
        Avaliacao.id == id
    ).first()

    if not avaliacao:
        raise HTTPException(404, "Avaliação não encontrada")

    db.delete(avaliacao)
    db.commit()

    return {"mensagem": "Avaliação removida com sucesso"}