import psycopg2 
from datetime import date

def get_conexao_postgres(banco_de_dados: str, usuario: str, senha: str ): #cria conexao

    conn = psycopg2.connect (
        database= 'contatos.bd', #nomedobd
        user= 'postgres', #usurario pgAdmin
        password= 'SENHA' #senhapgAdmin entrar
    )
    return conn #retornar conexao
'''
def executa_comando(conn, comando: str): #nsei praq serve ainda
    
    cur = conn.cursor()
    # executa um statement
    cur.execute(comando)
    
    cur.close()

''' 
#inserir registros bd 

def criar_tabela_aluno():
    conn= get_conexao_postgres("contatos", "postgres", "postgres")
    #criando tabela contatos
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE Contatos(
                   ID INTEGER PRIMARY KEY,
                   nome VARCHAR (100) NOT NULL,
                   DataNascimento DATE,
                   Telefone VARCHAR(20),
                   Rua VARCHAR(255),
                   NumeroResidencia VARCHAR(10),
                   Complemento VARCHAR(255),
                   Cidade VARCHAR(255),
                   Estado VARCHAR(50),
                   Pais VARCHAR(50),
                   CEP VARCHAR(10)
        );
    """)
    ID = 737289930
    nome = 'Beatriz'
    Datanascimento = date(2006, 7, 22)
    Telefone = '44 997200430'
    Rua = 'Ovidio da miami'
    NumeroResidencia = '254'
    Complemento = 'casa'
    Cidade = "Engenheiro Beltrão"
    Estado = 'Paraná'
    Pais = 'Brasil'
    CEP = '8727000'

    cursor.execute("""
            INSERT INTO Contatos (ID,nome,Datanascimento,Telefone,Rua,NumeroResidencia,Complemento,Cidade,Estado,Pais,CEP)
            VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s);
                   """,(ID,nome,Datanascimento,Telefone,Rua,NumeroResidencia,Complemento,Cidade,Estado,Pais,CEP))

    #INSERIR REGISTRO NA TABELA

    Contatos = [
        (635626793,'Fernanda',date(2007,7,22))
    ]
                   
                   
                

def main(): #valor na funcao de conexao
    conn = get_conexao_postgres("contatos", "postgres", "postgres")
    print(f'Conexão do tipo {str(type(conn))} criada com sucesso!')
    #db_version = executa_comando(conn, 'SELECT version()')
    conn.close() 

if __name__ == "__main__":
    main(); #chamando a main 


