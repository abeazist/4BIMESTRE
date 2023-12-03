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
    db_version = cur.fetchone()
    print(db_version)
    cur.close()

''' 
#inserir registros bd 

def criar_tabela_aluno():
    conn= get_conexao_postgres("contatos", "postgres", "postgres")
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE Contatos(
                   RA INTEGER PRIMARY KEY,
                   nome VARCHAR (100) NOT NULL,
                   
        )
                   
                   
                   
"""
                   )

def main(): #valor na funcao de conexao
    conn = get_conexao_postgres("contatos", "postgres", "postgres")
    print(f'Conexão do tipo {str(type(conn))} criada com sucesso!')
    #db_version = executa_comando(conn, 'SELECT version()')
    conn.close() 

if __name__ == "__main__":
    main(); #chamando a main 


