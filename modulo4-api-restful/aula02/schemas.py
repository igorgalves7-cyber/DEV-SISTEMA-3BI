from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


def _validar_nome(valor):
    """Regras de nome compartilhadas entre UsuarioCreate e UsuarioPatch."""
    if not isinstance(valor, str):
        raise ValueError("O nome deve ser um texto.")

    valor = valor.strip()

    if not valor:
        raise ValueError("O nome não pode ser vazio ou conter apenas espaços.")
    if len(valor) < 2:
        raise ValueError("O nome deve ter no mínimo 2 caracteres.")
    if len(valor) > 100:
        raise ValueError("O nome deve ter no máximo 100 caracteres.")
    if any(c.isdigit() for c in valor):
        raise ValueError("O nome não pode conter números.")

    return valor


class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="Nome do usuário (2–100 caracteres, sem números)")
    email: EmailStr = Field(..., description="E-mail válido")
    senha: str = Field(..., min_length=8, description="Mínimo 8 caracteres, com letra e número")

    # mode="before": remove espaços das bordas ANTES de o Field checar o tamanho
    @field_validator("nome", mode="before")
    @classmethod
    def validar_nome(cls, v):
        return _validar_nome(v)

    @field_validator("senha", mode="before")
    @classmethod
    def validar_senha(cls, v):
        if not isinstance(v, str):
            raise ValueError("A senha deve ser um texto.")
        if len(v) < 8:
            raise ValueError("A senha deve ter no mínimo 8 caracteres.")
        if not any(c.isalpha() for c in v):
            raise ValueError("A senha deve conter pelo menos uma letra.")
        if not any(c.isdigit() for c in v):
            raise ValueError("A senha deve conter pelo menos um número.")
        return v


class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None

    @field_validator("nome", mode="before")
    @classmethod
    def validar_nome(cls, v):
        if v is None:  # campo opcional: None é aceito
            return v
        return _validar_nome(v)


class UsuarioResponse(BaseModel):
    # Atenção: NUNCA incluir hash_senha aqui.
    id: int
    nome: str
    email: str
    ativo: bool
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)


class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None