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
    genero = Column(String(100), nullable=False)

    def __repr__(self):
        return f'id: {self.id_genero}, Gênero: {self.genero}' # como será printado


class Pessoa(Base):
    __tablename__ = 'pessoa'

    cod_pessoa = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

    filmes_participados = relationship('Filmes', secondary='pessoa_participa_filmes')
    series_participados = relationship('Serie', secondary='pessoa_participa_serie')

    def __repr__(self):
        return f'Id: {self.cod_pessoa}, Pessoas: {self.nome} {self.sobrenome}, Idade: {self.idade}'


class Filmes(Base):
    __tablename__  = 'filmes'

    cod_filme= Column(Integer, primary_key=True, nullable=False)
    titulo= Column(String,nullable=False)
    sinopse=Column(String,nullable=False)
    data_lancamento=Column(String,nullable=False)
    classificacao_etaria= Column(String,nullable=False)
    duracao_filme= Column(Integer,nullable=False)
    
    pessoas_participantes = relationship('Pessoa', secondary='pessoa_participa_filmes')
    
    def __repr__(self):
        return f'filmes {self.titulo}'


class Serie(Base):
    __tablename__ = 'series'

    cod_serie = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    sinopse = Column(String, nullable=False)
    data_lancamento = Column(DATE, nullable=False)
    data_encerramento = Column(DATE, nullable=False)
    classificacao_etaria = Column(String, nullable=False)
   
    serie_relacao = relationship('Pessoa', secondary='pessoa_participa_serie')
    
    def __repr__(self):
        return f'id_serie={self.cod_serie}, titulo={self.titulo}, sinopse={self.sinopse}, ' \
               f'data_lancamento={self.data_lancamento}, ' \
               f'data_encerramento={self.data_encerramento}' \
               f'classificacao_etaria={self.classificacao_etaria}, ' \


class Episodio(Base):
    __tablename__ = 'episodio'
    id_episodio = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(50), nullable=False)
    temporada = Column(Integer, nullable=False)

    def __repr__(self):
        return f'episodio {self.nome}'

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario= Column(Integer, primary_key=True, nullable=False)
    nome_usuario= Column(String, nullable=False)
    nick= Column(String, nullable= False)
    email= Column(String,nullable=False)
    senha= Column(String,nullable=False)
    data_de_registro= Column(DATE,nullable=False)
    avaliacao= Column(Integer,nullable=False)

    def __repr__(self):
        return f'usuario: {self.nome_usuario}'
    


class pessoa_participa_filmes(Base):
    __tablename__ = 'pessoa_participa_filmes'
    id_participa = Column(Integer, primary_key=True, nullable=False)
    cod_pessoa = Column(Integer, ForeignKey('pessoa.cod_pessoa'))
    cod_filme = Column(Integer, ForeignKey('filmes.cod_filme'))

    pessoa = relationship('Pessoa')
    filme = relationship('Filmes')


class pessoa_participa_serie(Base):
    __tablename__ = 'pessoa_participa_serie'
    id_participa = Column(Integer, primary_key=True, nullable=False)
    cod_pessoa = Column(Integer, ForeignKey('pessoa.cod_pessoa'))
    cod_serie = Column(Integer, ForeignKey('series.cod_serie'))

    pessoa = relationship('Pessoa')
    serie = relationship('Serie')


class serie_tem_episodio(Base):
    __tablename__ = 'serie_tem_episodio'
    id_serie_tem_episodio = Column(Integer, primary_key=True)
    cod_serie = Column(Integer, ForeignKey('series.cod_serie'), nullable=False)
    id_episodio = Column(Integer, ForeignKey('episodio.id_episodio'), nullable=False)

    serie = relationship('Serie')
    episodio = relationship('Episodio')


class avalia_filmes_usuario(Base):
    __tablename__ = 'avalia_filmes_usuario' 

    id_avalia_film= Column(Integer, primary_key=True,nullable=False)
    cod_filme = Column(Integer, ForeignKey('filmes.cod_filme')) 
    id_usuario= Column(Integer,ForeignKey('usuario.id_usuario')) 
    classificacao=Column(Integer) 
    comentario= Column(String(100))
    data_avaliacao = Column(DATE, nullable=False)

    filmes= relationship('Filmes')
    usuario= relationship ('Usuario')

    def __repr__(self):
        return f'Código filme {self.cod_filme} Id usuário: {self.id_usuario}'


class avalia_series_usuario(Base):
    __tablename__ = 'avalia_series_usuario'

    id_avalia_serie = Column(Integer, primary_key=True)
    cod_serie = Column(Integer, ForeignKey('series.cod_serie'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    classificacao = Column(Integer, nullable=False)
    comentario = Column(String(50))
    data_avaliacao = Column(DATE, nullable=False)

    serie = relationship('Serie')
    usuario = relationship('Usuario')
    def __repr__(self):
	    return f'cod_serie: {self.cod_serie}, usuario: {self.id_usuario}, classificacao: {self.classificacao}, comentario: {self.comentario}, data_avaliacao{self.data_avaliacao}'



#Base.metadata.create_all(engine)

#CREATE

def create_usuario():
    id_usuario = int(input("Entre com o id do usuario que deseja cadastrar: "))
    nome_usuario = input("Entre com o nome do usuario que deseja cadastrar: ")
    nick = input("Entre com o nick que deseja cadastrar: ")
    email = input("Entre com o email do usuario que deseja cadastrar: ")
    senha = input("Entre com a senha do usuario que deseja cadastrar: ")
    data_de_registro = input("Entre com a data de registro do usuario que deseja cadastrar: ")
    avaliacao = int(input("Entre com a avaliação do usuario que deseja cadastrar: "))

    user = Usuario(id_usuario = id_usuario, nome_usuario = nome_usuario, nick = nick, email = email, senha = senha, data_de_registro = data_de_registro, avaliacao = avaliacao)
    session.add(user)
    session.commit()
    print("Usuário criado com sucesso!")


def create_pessoa():
    cod_pessoa = int(input("Entre com o ID da pessoa que deseja cadastrar: "))

    nome = input("Entre com o nome da pessoa que deseja cadastrar: ")
    sobrenome = input("Entre com o sobrenome da pessoa que deseja cadastrar: ")
    idade = int(input("Entre com a idade da pessoa que deseja cadastrar: "))
    people = Pessoa(cod_pessoa=cod_pessoa, nome=nome, sobrenome=sobrenome, idade=idade)
    session.add(people)
    session.commit()
    print("Pessoa adicionada!")


def create_filme():
    cod_filme = int(input("Entre com o ID do filme que deseja cadastrar: "))
    titulo = input("Entre com o título do filme que deseja cadastrar: ")
    sinopse = input("Entre com a sinopse do filme que deseja cadastrar: ")
    data_lancamento = input("Entre com a data de lançamento do filme deseja cadastrar: ")
    classificacao_etaria = input("Entre com a classificacao etaria do filme que deseja cadastrar: ")
    duracao_filme = input("Entre com a duração do filme que deseja cadastrar(em minutos): ")

    movie = Filmes(cod_filme=cod_filme, titulo=titulo, sinopse=sinopse, data_lancamento=data_lancamento, classificacao_etaria=classificacao_etaria, duracao_filme = duracao_filme)
    session.add(movie)
    session.commit()
    print("Filme adicionado!")


def create_serie():
    cod_serie = int(input("Entre com o ID da série que deseja cadastrar: "))
    titulo = input("Entre com o título da série que deseja cadastrar: ")
    sinopse = input("Entre com a sinopse da série que deseja cadastrar: ")
    data_lancamento = input("Entre com a data de lançamento da série que deseja cadastrar: ")
    data_encerramento = input("Entre com a data de encerramento da série que deseja cadastrar: ")
    classificacao_etaria = int(input("Entre com a classificação etária da série que deseja cadastrar: "))


    program = Serie(cod_serie=cod_serie, titulo=titulo, sinopse=sinopse,data_lancamento=data_lancamento, data_encerramento=data_encerramento, classificacao_etaria=classificacao_etaria)
    session.add(program)
    session.commit()
    print("Série adicionada!")



#DELETES

#DELETE DE PESSOAS
# Função para excluir uma pessoa com base no ID
def excluir_pessoa():#caso não de certo tirar os parâmetros 
    cod_pessoa=int(input("Digite o cod_pessoa que deseja deletar: "))
    pessoa_excluir = session.query(Pessoa).filter_by(cod_pessoa=cod_pessoa).first()
    
    if pessoa_excluir:
        session.delete(pessoa_excluir)
        session.commit()
        print(f'Pessoa com cod_pessoa {pessoa_excluir} excluída com sucesso.')
    else:
        print(f'Pessoa com cod_pessoa {pessoa_excluir} não encontrada.')


#DELETE DE FILME
# Função para excluir um filme com base no ID
def excluir_filme():#caso não de certo tirar os parâmetros 
    cod_Filme=int(input("Digite o cod_filme que deseja deletar: "))
    filme = session.query(Filmes).filter_by(cod_filme=cod_Filme).first()
    if filme:
        session.delete(filme)
        session.commit()
        print(f'Filme com cod_filme {filme} excluído com sucesso.')
    else:
        print(f'Filme com cod_filme {filme} não encontrado.')


#DELETE DE SERIE
# Função para excluir uma série com base no ID
def excluir_serie(): #caso não de certo tirar os parâmetros 
    cod_Serie=int(input("Digite o cod_serie que deseja deletar: "))
    serie = session.query(Serie).filter_by(cod_serie=cod_Serie).first()
    if serie:
        session.delete(serie)
        session.commit()
        print(f'Série com cod_serie {serie} excluída com sucesso.')
    else:
        print(f'Série com cod_serie {serie} não encontrada.')

#DELETE DE USUARIO
def excluir_usuario():
    id_Usuario=int(input("Digite o id_usuario que deseja deletar: "))
    usuario= session.query(Usuario).filter_by(id_usuario=id_Usuario).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário {usuario} excluído com sucesso.')
    else:
        print(f'usuário {usuario} não encontrado.')



#UPDATE

def atualizar_serie():
    # Solicitar o título da série a ser atualizada
    serie_titulo = input("Digite o nome da série que deseja atualizar: ")

    # Buscar a série no banco de dados
    serie_encontrada = session.query(Serie).filter_by(titulo=serie_titulo).first()

    if serie_encontrada:
        # Exibir informações da série encontrada
        print(f'Informações da Série a ser Atualizada: ', serie_encontrada)

        # Solicitar os novos atributos
        novo_titulo = input("Digite o novo título da série: ")
        nova_sinopse = input("Digite a nova sinopse da série: ")
        nova_data_lancamento = input("Digite a nova data de lançamento da série (no formato YYYY-MM-DD): ")
        nova_data_encerramento = input("Digite a nova data de encerramento da série (no formato YYYY-MM-DD): ")
        nova_classificacao_etaria = input("Digite a nova classificação etária da série: ")

        # Atualizar os atributos da série
        serie_encontrada.titulo = novo_titulo
        serie_encontrada.sinopse = nova_sinopse
        serie_encontrada.data_lancamento = nova_data_lancamento
        serie_encontrada.data_encerramento = nova_data_encerramento
        serie_encontrada.classificacao_etaria = nova_classificacao_etaria

        # Commit da transação
        session.commit()

        print(f'Série "{serie_titulo}" atualizada com sucesso. Novos atributos: Título: {novo_titulo}, Sinopse: {nova_sinopse}, Data de Lançamento: {nova_data_lancamento}, Data de Encerramento: {nova_data_encerramento}, Classificação Etária: {nova_classificacao_etaria}')
    else:
        print(f'Série "{serie_titulo}" não encontrada.')


def atualizar_pessoa():
    pessoa_id = int(input("Digite o ID da pessoa que deseja atualizar: "))
    
    pessoa_encontrada = session.query(Pessoa).filter_by(cod_pessoa=pessoa_id).first()

    if pessoa_encontrada:
        print(f'Informações da Pessoa a ser Atualizada: ', pessoa_encontrada)

       
        novo_nome = input("Digite o novo nome da pessoa: ")

      
        novo_sobrenome = input("Digite o novo sobrenome da pessoa: ")

       
        nova_idade = int(input("Digite a nova idade da pessoa: "))

      
        pessoa_encontrada.nome = novo_nome
        pessoa_encontrada.sobrenome = novo_sobrenome
        pessoa_encontrada.idade = nova_idade

        
        session.commit()

        print(f'Pessoa com ID "{pessoa_id}" atualizada com sucesso. Novo nome: {novo_nome}, Novo sobrenome: {novo_sobrenome}, Nova idade: {nova_idade}')
    else:
        print(f'Pessoa com ID "{pessoa_id}" não encontrada.')


def atualizar_filme():
    
    filme_titulo = input("Digite o título do filme que deseja atualizar: ")
    
     
    filme_encontrado = session.query(Filmes).filter_by(titulo=filme_titulo).first()

    if filme_encontrado:
         
        print(f'Informações do Filme a ser Atualizado: ', filme_encontrado)

        
        novo_titulo = input("Digite o novo título do filme: ")

         
        nova_sinopse = input("Digite a nova sinopse do filme: ")

        
        nova_data_lancamento = input("Digite a nova data de lançamento do filme: ")

 
        nova_classificacao_etaria = input("Digite a nova classificação etária do filme: ")

         
        nova_duracao_filme = int(input("Digite a nova duração do filme (em minutos): "))

      
        filme_encontrado.titulo = novo_titulo
        filme_encontrado.sinopse = nova_sinopse
        filme_encontrado.data_lancamento = nova_data_lancamento
        filme_encontrado.classificacao_etaria = nova_classificacao_etaria
        filme_encontrado.duracao_filme = nova_duracao_filme

      
        session.commit()

        print(f'Filme "{filme_titulo}" atualizado com sucesso. Novo título: {novo_titulo}, Nova sinopse: {nova_sinopse}, Nova data de lançamento: {nova_data_lancamento}, Nova classificação etária: {nova_classificacao_etaria}, Nova duração: {nova_duracao_filme} minutos')
    else:
        print(f'Filme "{filme_titulo}" não encontrado.')


def atualizar_usuario():
    usuario_id = int(input("Digite o ID do usuário que deseja atualizar: "))
    
    usuario_encontrado = session.query(Usuario).filter_by(id_usuario=usuario_id).first()

    if usuario_encontrado:
        print(f'Informações do Usuário a ser Atualizado: ', usuario_encontrado)
        novo_nome_usuario = input("Digite o novo nome de usuário: ")
        novo_nick = input("Digite o novo nick: ")
        novo_email = input("Digite o novo e-mail: ")
        nova_senha = input("Digite a nova senha: ")

        # Solicitar a nova data de registro
        nova_data_registro = input("Digite a nova data de registro (no formato YYYY-MM-DD): ")
        nova_avaliacao = int(input("Digite a nova avaliação: "))
        usuario_encontrado.nome_usuario = novo_nome_usuario
        usuario_encontrado.nick = novo_nick
        usuario_encontrado.email = novo_email
        usuario_encontrado.senha = nova_senha
        usuario_encontrado.data_de_registro = nova_data_registro
        usuario_encontrado.avaliacao = nova_avaliacao

       
        session.commit()

        print(f'Usuário com ID {usuario_id} atualizado com sucesso. Novo nome de usuário: {novo_nome_usuario}, Novo nick: {novo_nick}, Novo e-mail: {novo_email}, Nova senha: {nova_senha}, Nova data de registro: {nova_data_registro}, Nova avaliação: {nova_avaliacao}')
    else:
        print(f'Usuário com ID {usuario_id} não encontrado.')

#READ

def procurar_usuario():
    usuario_id= int(input("Digite o ID do usuário que deseja obter:"))
    usuario=session.query (Usuario).filter_by(id_usuario=usuario_id).first()
    if usuario:
        print("Usuario encontrado!!",usuario)
    else:
       print("Usuario não encontrado.")

#TABELA SERIE
def procurar_serie():
    serie_pesquisar = input("Digite o nome da serie que deseja obter informações: ")
    serie_encontrado = session.query(Serie).filter_by(titulo=serie_pesquisar).first()

    if serie_encontrado:
        print('Informações da Serie: ', serie_encontrado)
    else:
        print(f'Serie "{serie_pesquisar}" não encontrado.')

#  TABELA FILMES
def procurar_filme():
    filme_pesquisar = input("Digite o nome do filme que deseja obter informações: ")
    filme_encontrado = session.query(Filmes).filter_by(titulo=filme_pesquisar).first()

    if filme_encontrado:
        print('filme encontrado!!',filme_encontrado)
    else:
        print(f'Filme:"{filme_pesquisar}" não encontrado.')

def procurar_pessoa():
    pessoa_pesquisar= int(input("Digite o ID da pessoa que deseja obter:"))
    pessoa_encontrada =session.query (Pessoa).filter_by(cod_pessoa=pessoa_pesquisar).first()
    if pessoa_encontrada:
        print("Pessoa encontrada!!",pessoa_encontrada)
    else:
       print("Pessoa não encontrada.")

print("CONSULTAS")
#SELECIONE TODOS OS USUARIOS QUE AVALIARAM FILMES COM MAIS DE 3 ESTRELAS
# Execute a consulta utilizando a API de consulta do SQLAlchemy
resultados = (
    session.query(Usuario.id_usuario, Usuario.nome_usuario, Filmes.titulo)
    .join(avalia_filmes_usuario, Usuario.id_usuario == avalia_filmes_usuario.id_usuario)
    .join(Filmes, Filmes.cod_filme == avalia_filmes_usuario.cod_filme)
    .filter(avalia_filmes_usuario.classificacao > 3)
    .order_by(Usuario.id_usuario, Filmes.titulo)
    .all()
)

# Exiba os resultados
for resultado in resultados:
    print(f'ID: {resultado.id_usuario}, Nome de Usuário: {resultado.nome_usuario}, Filme: {resultado.titulo}')

#SELECIONE TODAS AS PESSOAS QUE ESTÃO PARTICIPANDO DE TITANIC

#SELECIONE TODOS os USUARIOS EXISTENTES
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f'ID: {usuario.id_usuario}, Nome de Usuário: {usuario.nome_usuario}, Nick: {usuario.nick}')

#SELECIONE O NOME DE TODAS AS PESSOAS QUE PARTICIPAM DE SEUS RESPSECTIVOS FILMES
resultados = (
    session.query(Pessoa.nome, Filmes.titulo)
    .join(pessoa_participa_filmes, Pessoa.cod_pessoa == pessoa_participa_filmes.cod_pessoa)
    .join(Filmes, Filmes.cod_filme == pessoa_participa_filmes.cod_filme)
    .order_by(Pessoa.nome, Filmes.titulo)
    .all()
)

# Exiba os resultados
for resultado in resultados:
    print(f'Nome: {resultado.nome}, Filme: {resultado.titulo}')
# #MENU

print("O que você gostaria de fazer?")
print("1 - Cadastrar")
print("2 - Procurar")
print("3 - Atualizar")
print("4 - Deletar")

escolha = input("Digite o número da opção desejada: ")
if escolha == "1":

    print("Escolha uma subopção:")
    print("1 - Série")
    print("2 - Filme")
    print("3 - Pessoa")
    print("4 - Usuário")

    subescolha = input("Digite o número da subopção desejada: ")

    if subescolha == "1":
        create_serie()

    elif subescolha == "2":
        create_filme()
        
    elif subescolha == "3":
        create_pessoa()
    
    elif subescolha == "4":
        create_usuario()
        
    else:
        print("Opção inválida.")

elif escolha == "2":
    print('Você escolheu Procurar')
    print("1 - Série")
    print("2 - Filme")
    print("3 - Pessoa")
    print("4 - Usuário")

    dado_procurado = input("Digite o que deseja procurar: ")
    
    if dado_procurado == "1":
        procurar_serie()

    elif dado_procurado == "2":
        procurar_filme()
        
    elif dado_procurado == "3":
        procurar_pessoa()
    
    elif dado_procurado == "4":
        procurar_usuario()
        
    else:
        print("Opção inválida.")

elif escolha == "3":
    print("Você escolheu Atualizar.")
    print("1 - Série")
    print("2 - Filme")
    print("3 - Pessoa")
    print("4 - Usuário")
    informacao = input("Digite o dado que você deseja atualizar: ")

    if informacao == "1":
        atualizar_serie()
        
    elif informacao == "2":
        atualizar_filme()
        
    elif informacao == "3":   
        atualizar_pessoa()  
    
    elif informacao == "4":
        atualizar_usuario()
      
    else:
        print("Opção inválida.")

elif escolha == "4":
    print("Você escolheu Deletar")
    print("1 - Série")
    print("2 - Filme")
    print("3 - Pessoa")
    print("4 - Usuário")
    delete = input("Escolha o que você quer deletar:")

    if delete == "1":
        excluir_serie()
        
    elif delete == "2":
        excluir_filme()
        
    elif delete == "3":
        excluir_pessoa()
    
    elif delete == "4":
        excluir_usuario()
        
    else:
        print("Opção inválida.")