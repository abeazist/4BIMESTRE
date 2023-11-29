import sqlalchemy

from sqlalchemy import create_engine,Column,Integer,String,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://:memory:', echo= True)
session = sessionmaker(bind=engine)
chamaSession = session()
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
        return f'filmes {self.titulo}'



    


