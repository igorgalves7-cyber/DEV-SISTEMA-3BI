from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict


# --- ENUMS ---

class StatusEnum(str, Enum):
    pendente = 'pendente'
    em_andamento = 'em_andamento'
    concluida = 'concluida'
    cancelada = 'cancelada'


class PrioridadeEnum(str, Enum):
    baixa = 'baixa'
    media = 'media'
    alta = 'alta'
    critica = 'critica'


# --- SCHEMAS DE TAREFA ---

class TarefaEntrada(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={'example': {
            'titulo': 'Implementar autenticacao JWT',
            'descricao': 'Adicionar login com token na API',
            'responsavel': 'Carlos Silva',
            'prioridade': 'alta',
            'prazo': '2025-12-31',
            'tags': ['Backend', 'JWT']
        }}
    )
    titulo: str
    descricao: Optional[str] = None
    responsavel: Optional[str] = None
    prioridade: PrioridadeEnum = PrioridadeEnum.media
    status: StatusEnum = StatusEnum.pendente
    prazo: Optional[date] = None
    tags: list[str] = Field(default_factory=list)  # Parte 2.b: padrão lista vazia

    @field_validator('titulo')
    @classmethod
    def validar_titulo(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 caracteres')
        if len(v) > 120:
            raise ValueError('O titulo deve ter no maximo 120 caracteres')
        return v

    @field_validator('responsavel')
    @classmethod
    def validar_responsavel(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            v = v.strip()
            if len(v) < 2:
                raise ValueError('Nome do responsavel deve ter pelo menos 2 caracteres')
            return v.title()
        return v

    # Parte 2.b: Validador para converter tags para minúsculo e remover duplicatas
    @field_validator('tags')
    @classmethod
    def normalizar_tags(cls, tags: list[str]) -> list[str]:
        return list({tag.lower().strip() for tag in tags if tag.strip()})


class TarefaSaida(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    responsavel: Optional[str] = None
    prioridade: PrioridadeEnum
    status: StatusEnum
    prazo: Optional[date] = None
    tags: list[str] = Field(default_factory=list)  # Parte 2.b
    criado_em: date = Field(default_factory=date.today)  # Parte 2.a: data atual padrão


class TarefaParcial(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    responsavel: Optional[str] = None
    prioridade: Optional[PrioridadeEnum] = None
    status: Optional[StatusEnum] = None
    prazo: Optional[date] = None
    tags: Optional[list[str]] = None


# Parte 1.b: Schema exclusivo para a rota PATCH de atualização de status
class StatusUpdate(BaseModel):
    status: StatusEnum


# --- DESAFIO EXTRA: SCHEMAS DE COMENTÁRIO ---

class ComentarioEntrada(BaseModel):
    autor: str
    texto: str


class Comentario(ComentarioEntrada):
    id: int
    tarefa_id: int