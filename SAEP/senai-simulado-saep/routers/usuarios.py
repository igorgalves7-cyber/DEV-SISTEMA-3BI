from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


class UsuarioCreate(BaseModel):
    nome: str
    login: str
    perfil: str


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    login: Optional[str] = None
    perfil: Optional[str] = None


def buscar_usuario(db: Session, id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()


@router.get("/{id}")
def obter(id: int, db: Session = Depends(get_db)):
    return buscar_usuario(db, id)


@router.post("/", status_code=201)
def criar(dados: UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(models.Usuario).filter(models.Usuario.login == dados.login).first():
        raise HTTPException(status_code=409, detail="Login já cadastrado")
    usuario = models.Usuario(**dados.model_dump())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


@router.put("/{id}")
def atualizar(id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = buscar_usuario(db, id)
    campos = dados.model_dump(exclude_unset=True)
    if "login" in campos:
        outro = db.query(models.Usuario).filter(
            models.Usuario.login == campos["login"], models.Usuario.id != id
        ).first()
        if outro:
            raise HTTPException(status_code=409, detail="Login já cadastrado")
    for campo, valor in campos.items():
        setattr(usuario, campo, valor)
    db.commit()
    db.refresh(usuario)
    return usuario


@router.delete("/{id}")
def remover(id: int, db: Session = Depends(get_db)):
    usuario = buscar_usuario(db, id)
    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário removido"}