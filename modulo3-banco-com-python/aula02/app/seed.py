from app.database import SessionLocal, Base, engine
from app.models import Departamento, Cargo, Funcionario


def popular_banco():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()   # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])
        db.add_all([
    Funcionario(nome='Igor Gabriel', email='igor.gabriel@empresa.com', telefone='47912345678', salario=4700.00),
    Funcionario(nome='Sarah Isabela', email='sarah.isabela@empresa.com', telefone='21998765432', salario=3300.00),
    Funcionario(nome='Enzo Peres', email='enzo.peres@empresa.com', telefone='31987654321', salario=7100.00),
    Funcionario(nome='Thiago Henrique', email='thiago.henrique@empresa.com', telefone='11976543210', salario=3050.00),
])

        db.commit()     # confirma tudo no banco de uma vez
        print('Banco preenchido com sucesso')

    except Exception as erro:
        db.rollback()   # desfaz tudo se der erro
        print(f'Erro: {erro}')
    finally:
        db.close()      # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()