# API Loja de Games

API RESTful para gerenciar o catálogo de uma loja de games; plataformas, jogos e avaliações dos clientes.

---

## Tecnologias utilizadas
- Python 3
- FastAPI 
- SQLAlchemy
- Pydantic
- Uvicorn

---
## Como instalar e executar
1. Clone o repositório e entre na pasta do projeto:
```
git clone https://github.com/MMVonnSeek/dev-sistemas.git
cd loja-games
```
2. Crie e ative o ambiente virtual (venv)
```
python -m venv venv
source venv/Scripts/activate
```

3. Instale as dependências:
```
pip install fastapi uvicorn sqlalchemy
```

4. Execute o servidor:
```
uvicorn main:app --reload
```

5. Acesse a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs

---
## Rotas da API
| Método | Rotas | O que faz |
| --- | --- |---|
|GET | `/plataforma/` | Lista todas as plataformas |
| POST | `/plataforma` | Cadastra uma nova plataforma |
| GET | `/jogos/` | Lista todos os jogos |
| GET | `/jogos{id}` | Busca um jogo pelo ID |
| POST | `/jogos/` | Cadastra um novo jogo |
| PUT | `/jogos{id}/` | Atualiza os dados de um jogo |
| DELETE | `/jogos{id}/` | Remove um jogo |
| GET | `/Jogos/{id}/avaliacoes` | Lista as avaliações de um jogo |
| POST | `/avaliacoes/` | Registra uma avaliação |
| DELETE | `/avaliacoes/{id}/` | Remove uma avaliação |

---

## Autor
Max Muller - Desenvolvimento de Sistemas - SENAI - DF