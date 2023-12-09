from sqlalchemy import create_engine,Column,Integer,String,Date from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@localhost/IMDbtrabalho3bime', echo= True)
Session = sessionmaker(bind=engine)
chamaSession = Session()
Base = declarative_base()
'''
class criarConexao:
    def__init__(self):
    self._connection_string = 'postgressql://postgres:postgres@localhost:5432/IMDbtrabalho3bime'
    # self._connection_string = 'postgresql://abeazist:2DuChAswiO1F@ep-wild-field-92098951.us-east-2.aws.neon.tech/IMDb_trabalho3bime?sslmode=require'
    
'''

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
        return f'usuario {self.nome_usuario}'
    
class filmes(Base):
    __tablename__  = 'filmes'

    cod_filme= Column(Integer,nullable=False)
    titulo= Column(String,nullable=False)
    sinopse=Column(String,nullable=False)
    data_lanc=Column(String,nullable=False)
    classificacao_etaria= Column(String,nullable=False)
    duracao_filme= Column(Integer,nullable=False)
    
    def __repr__(self):
        return f'filmes {self.titulo}'; 

class avalia_filmes_usuario(Base): 
    __tablename__ = 'avalia_filmes_usuario' 

    classificacao=Column(Integer)
    comentario= Column(String (100)) 
    data_avaliacao= Column(DATE)
    cod_filme = Column(Integer, ForeignKey('filmes.cod_filme'))
    filmes = relationship('Filmes')
    id_usuario= Column(Integer, ForeignKey('usuarios.id_usuario')) 
    usuario= relationship ('usuario')
    
 
Base.metadata.create_all(engine)

#consultas 
query = session.query(Filmes).filter_by(datalanc>"01/01/1999")
query = session.query(Atores).filter_by(sexo = "F")

