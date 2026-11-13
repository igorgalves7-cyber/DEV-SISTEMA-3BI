from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from database import get_db
from models import Plataforma

router = APIRouter(prefix="/plataformas", tags=["Plataformas"])


class PlataformaCreate(BaseModel):
    nome: str


@router.get("/")
def listar_plataformas(db: Session = Depends(get_db)):
    return db.query(Plataforma).all()


@router.post("/")
def cadastrar_plataforma(
    plataforma: PlataformaCreate,
    db: Session = Depends(get_db)
):
    nova = Plataforma(nome=plataforma.nome)
    db.add(nova)

    try:
        db.commit()
        db.refresh(nova)
    except IntegrityError:
        db.rollback()
        raise HTTPException(400, "Essa plataforma já está cadastrada")

    return nova