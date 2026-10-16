from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class LivroCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=200)
    autor: str = Field(..., min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None


class LivroUpdate(BaseModel):
    """Todos os campos são opcionais: só o que for enviado será atualizado."""

    titulo: Optional[str] = Field(None, min_length=2, max_length=200)
    autor: Optional[str] = Field(None, min_length=2, max_length=150)
    ano_publicacao: Optional[int] = None
    disponivel: Optional[bool] = None

    @model_validator(mode="after")
    def campos_obrigatorios_nao_nulos(self):
        # titulo, autor e disponivel não aceitam null explícito
        for campo in ("titulo", "autor", "disponivel"):
            if campo in self.model_fields_set and getattr(self, campo) is None:
                raise ValueError(f"'{campo}' não pode ser nulo")
        return self


class LivroResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    autor: str
    ano_publicacao: Optional[int]
    disponivel: bool
    criado_em: datetime