from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/movimentacoes", tags=["Movimentações"])


class MovimentacaoCreate(BaseModel):
    tipo: str
    quantidade: float
    observacao: Optional[str] = None
    produto_id: int
    usuario_id: int


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(models.Movimentacao).all()


@router.get("/{id}")
def obter(id: int, db: Session = Depends(get_db)):
    mov = db.query(models.Movimentacao).filter(models.Movimentacao.id == id).first()
    if not mov:
        raise HTTPException(status_code=404, detail="Movimentação não encontrada")
    return mov


@router.post("/", status_code=201)
def criar(dados: MovimentacaoCreate, db: Session = Depends(get_db)):
    if not db.query(models.Produto).filter(models.Produto.id == dados.produto_id).first():
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if not db.query(models.Usuario).filter(models.Usuario.id == dados.usuario_id).first():
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    mov = models.Movimentacao(**dados.model_dump())
    db.add(mov)
    db.commit()
    db.refresh(mov)
    return mov