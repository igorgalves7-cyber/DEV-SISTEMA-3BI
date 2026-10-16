from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco - SQLite salva em um arquivo banco.db na pasta d projeto
DATABASE_URL = 'sqllite:///./banco.db'

# Engine: motor de conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False} # necessario para SQL
)

# SessionLoacal: fábrica de sessões - cada requisições tem a sua própria
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base: classe base que todos os modelos vão herdar
Base = declarative_base()

# Dependência injetada nos endpoints via Depends(get_db)
# yeld entrega a sessão - endpoint executa - finally fecha a sessão
def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
         db.close()     