# 🎮 Loja de Games API

## Descrição do projeto

A Loja de Games API é uma aplicação desenvolvida em Python utilizando FastAPI, com o objetivo de gerenciar plataformas de jogos, jogos cadastrados e avaliações dos usuários.

A API permite cadastrar, consultar, atualizar e excluir informações, facilitando o gerenciamento de uma loja de games.

## Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **FastAPI:** framework utilizado para criação da API.
- **Uvicorn:** servidor utilizado para executar a aplicação.
- **SQLAlchemy:** ferramenta utilizada para comunicação com o banco de dados.
- **Pydantic:** utilizado para validação dos dados.
- **SQLite:** banco de dados utilizado para armazenar as informações.

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/igorgalves7-cyber/DEV-SISTEMA-3BI/tree/main/modulo4-api-restful/PROVA/loja-games-api
```

### 2. Entrar na pasta do projeto

```bash
cd loja-games-api
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a API

```bash
uvicorn main:app --reload
```

Após iniciar, acesse:

- API: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs

## Rotas da API

### Plataformas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/plataformas/` | Lista todas as plataformas cadastradas. |
| POST | `/plataformas/` | Cadastra uma nova plataforma. |

### Jogos

| Método | Rota | Descrição |
|---|---|---|
| GET | `/jogos/` | Lista todos os jogos. |
| GET | `/jogos/{id}` | Busca um jogo pelo ID. |
| POST | `/jogos/` | Cadastra um novo jogo. |
| PUT | `/jogos/{id}` | Atualiza os dados de um jogo. |
| DELETE | `/jogos/{id}` | Remove um jogo. |
| GET | `/jogos/{id}/avaliacoes` | Lista as avaliações de um jogo. |

### Avaliações

| Método | Rota | Descrição |
|---|---|---|
| POST | `/avaliacoes/` | Registra uma avaliação para um jogo. |
| DELETE | `/avaliacoes/{id}` | Remove uma avaliação pelo ID. |

## Autor

**Igor Gabriel**

Projeto desenvolvido como parte do projeto final do Módulo 4.