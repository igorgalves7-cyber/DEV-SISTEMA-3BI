from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class StatusEnum(str, Enum):
    PENDENTE = "pendente"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"


class PrioridadeEnum(str, Enum):
    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"


class TarefaEntrada(BaseModel):
    titulo: str
    descricao: str | None = None
    responsavel: str
    prioridade: PrioridadeEnum = PrioridadeEnum.MEDIA
    tags: list[str] = Field(default_factory=list)

    @field_validator("tags")
    @classmethod
    def normalizar_tags(cls, tags: list[str]) -> list[str]:
        # Converte para minúsculo e remove duplicatas mantendo tipo list
        return list({tag.lower().strip() for tag in tags})


class TarefaSaida(TarefaEntrada):
    id: int
    status: StatusEnum = StatusEnum.PENDENTE
    criado_em: date = Field(default_factory=date.today)


class StatusUpdate(BaseModel):
    status: StatusEnum


# Modelo do Desafio Extra
class ComentarioEntrada(BaseModel):
    autor: str
    texto: str


class Comentario(ComentarioEntrada):
    id: int
    tarefa_id: int