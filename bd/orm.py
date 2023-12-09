from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, DATE  
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('postgresql://postgres:postgres@localhost:5432/IMDb_trabalho3bime', echo=True) 
from datetime import datetime
#'postgresql://seu_usuario:senha@localhost/nome_do_banco'
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

'''entidades'''


class Genero(Base):
    __tablename__ = 'genero'

    id_genero = Column(Integer, primary_key=True, nullable=False)
    genero = Column(String, nullable=False)

    def __repr__(self):
        return f'id: {self.id_genero}, Gênero: {self.genero}' # como será printado


class Pessoa(Base):
    __tablename__ = 'pessoa'

    cod_pessoa = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Id: {self.cod_pessoa}, Pessoas: {self.nome} {self.sobrenome}, Idade: {self.idade}'
    


class Filmes(Base):
    __tablename__  = 'filmes'

    cod_filme= Column(Integer, primary_key=True, nullable=False)
    titulo= Column(String,nullable=False)
    sinopse=Column(String,nullable=False)
    data_lanc=Column (DATE,nullable=False)
    classificacao_etaria= Column(String,nullable=False)
    duracao_filme= Column(Integer,nullable=False)
    
    def __repr__(self):
        return f'filmes {self.titulo}'


class Serie(Base):
    __tablename__ = 'series'

    id_serie = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    sinopse = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    data_lancamento = Column(DATE, nullable=False)
    data_encerramento = Column(DATE, nullable=False)
    temporadas = Column(Integer, nullable=False)
    classificacao_etaria = Column(String, nullable=False)
    elenco = Column(String, nullable=True)
    avaliacao_media = Column(Integer, nullable=True)

    # diretor_id = Column(Integer, ForeignKey('diretores.id_diretor'))
    # diretor = relationship('Diretor', back_populates='series')
		#ATT NANDA: VOU VERIFICAR SOBRE AS RELAÇÕES HOJE 09/12

    def __repr__(self):
        return f'Serie(id_serie={self.id_serie}, titulo={self.titulo}, sinopse={self.sinopse}, ' \
               f'genero={self.genero}, data_lancamento={self.data_lancamento}, ' \
               f'data_encerramento={self.data_encerramento}, temporadas={self.temporadas}, ' \
               f'classificacao_etaria={self.classificacao_etaria}, elenco={self.elenco}, ' \
               f'avaliacao_media={self.avaliacao_media}, diretor={self.diretor})'
    

class Episodio(Base):
    __tablename__ = 'episodio'
    id_episodio = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    temporada = Column(Integer, nullable=False)

    def __repr__(self):
         return f'episodio {self.nome}'

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario= Column(Integer,primary_key=True)
    nome_usuario= Column(String, nullable=False)
    nick= Column(String, nullable= False)
    email= Column(String,nullable=False)
    senha= Column(String,nullable=False)
    data_de_registro= Column(DATE,nullable=False)
    avaliacao= Column(Integer,nullable=False)

    def __repr__(self):
        return f'usuario {self.nome_usuario}'
    
class Avalia_filmes_usuario(Base):
    __tablename__ = 'avalia_filmes_usuario' 

    id_avalia_film= Column(Integer, primary_key=True,nullable=False)
    classificacao=Column(Integer) 
    cod_filme = Column(Integer, ForeignKey('filmes.cod_filme')) 
    filmes= relationship('Filmes')
    id_usuario= Column(Integer,ForeignKey('usuario.id_usuario')) 
    usuario= relationship ('Usuario')

Base.metadata.create_all(engine)



#consultas abea
#filmes_lancados_apos_1999 = session.query(Filmes).filter(Filmes.data_lanc > datetime.strptime('1999-01-01', '%Y-%m-%d'))
pessoas = session.query(Pessoa).filter(Pessoa.nome.ilike == '%i%')

for i in pessoas:
    print(f'Nome: {i.nome}, Sobrenome: {i.sobrenome}')

#session.close()