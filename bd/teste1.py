from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.declarative import declarative_base
from datetime import date 

# Substitua 'postgresql://seu_usuario:senha@localhost/seu_banco_de_dados' pelos detalhes reais do seu banco de dados PostgreSQL
db_url = 'postgresql://postgres:postgres@localhost/IMDbtrabalho3bime'

try:
    # Tentar criar a engine e estabelecer a conexão
    engine = create_engine(db_url, echo=True)
    connection = engine.connect()
    print("Conexão bem-sucedida com o banco de dados PostgreSQL!")

    # Definir a classe de modelo
    Base = declarative_base()

    class usuario(Base):
        __tablename__ = 'usuario'

        id_usuario= Column(Integer,primary_key=True)
        nome_usuario= Column(String, nullable=False)
        nick= Column(String, nullable= False)
        email= Column(String,nullable=False)
        senha= Column(String,nullable=False)
        data_de_registro= Column(Date,nullable=False)
        avaliacao= Column(Integer,nullable=False)

        def __repr__(self):
            return f'usuario {self.nome_usuario}';

    class filmes(Base):
        __tablename__ = 'filmes'
        cod_filme = Column(Integer, primary_key=True)
        titulo = Column(String(100))
        cod_filme = Column(Integer)
        sinopse = Column(String(200))
        # Adicione mais colunas conforme necessário

    # Exemplo de instrução DROP TABLE IF EXISTS
    metadata = MetaData()
    usuario_table = Table('usuario', metadata, autoload_with=engine)
    usuario_table.drop(engine, checkfirst=True)

    # Criar as tabelas no banco de dados
    Base.metadata.create_all(engine)

    # Criar uma sessão para interagir com o banco de dados
    Session = sessionmaker(bind=engine)
    session = Session()

    # Exemplo de inserção de dados
    '''
    novo_filme = Filme(titulo="Filme Teste", cod_filme=1, sinopse="Uma sinopse de teste")
    session.add(novo_filme)
    session.commit()

    print("Dados inseridos com sucesso!")
    '''

except OperationalError as e:
    print(f"Erro na conexão: {e}")