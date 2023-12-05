import psycopg2 
from datetime import date

#cria conexao a)
def get_conexao_postgres(banco_de_dados: str, usuario: str, senha: str ):

    conn = psycopg2.connect (
        database= 'contatos.bd', #nomedobd
        user= 'postgres', #usurario pgAdmin
        password= 'postgres' #senhapgAdmin entrar
    )
    return conn #retornar conexao
'''
def executa_comando(conn, comando: str): #nsei praq serve ainda
    
    cur = conn.cursor()
    # executa um statement
    cur.execute(comando)
    
    cur.close()
'''


''''''
#criando tabela b)
def criar_tabela_contatos():
    conn= get_conexao_postgres("Contatos", "postgres", "postgres")
    #criando tabela contatos
    cursor=conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Contatos;
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

    #INSERIR REGISTRO NA TABELA c)

    Contatos = [
        (737289933, 'Isabela',1998-3-10, '33 987654321', 'Rua K, 987', '789', 'Apartamento 502', "Curitiba", 'Paraná', 'Brasil', '8765432'),
        (737289934, 'Miguel Oliveira', 2005-11-18, '22 876543210', 'Avenida Central, 456', '456', 'Casa 101', "Rio de Janeiro", 'Rio de Janeiro', 'Brasil', '4567890'),
        (737289935, 'Laura Pereira', date(2000, 11, 18), '11 765432109', 'Rua L, 654', '321', 'Sem complemento', "Belo Horizonte", 'Minas Gerais', 'Brasil', '3456789'),
        (737289936, 'Gustavo Silva', date(1993, 2, 28), '44 654321098', 'Avenida M, 789', '987', 'Bloco 3, Apt 201', "Porto Alegre", 'Rio Grande do Sul', 'Brasil', '2345678'),
        (737289937, 'Sophia Santos', date(2002, 6, 8), '55 543210987', 'Rua N, 1011', '121', 'Casa 5', "Salvador", 'Bahia', 'Brasil', '7890123'),
        (737289938, 'Daniel Costa', date(1995, 1, 30), '33 432109876', 'Rua O, 1213', '1314', 'Apartamento 404', "Recife", 'Pernambuco', 'Brasil', '8901234'),
        (737289939, 'Valentina Rodrigues', date(1988, 7, 12), '11 321098765', 'Avenida P, 1415', '1516', 'Casa 707', "Fortaleza", 'Ceará', 'Brasil', '9012345'),
        (737289940, 'Ricardo Nunes', date(1996, 4, 22), '44 210987654', 'Rua Q, 1617', '1718', 'Apartamento 606', "Manaus", 'Amazonas', 'Brasil', '5678901'),
        (737289941, 'Isadora Souza', date(1989, 8, 6), '22 109876543', 'Avenida R, 1819', '1920', 'Casa 808', "Natal", 'Rio Grande do Norte', 'Brasil', '2109876'),
        (737289942, 'Leonardo Almeida', date(1997, 12, 15), '33 876543210', 'Rua S, 2021', '2122', 'Apartamento 909', "Brasília", 'Distrito Federal', 'Brasil', '1098765')

    ]
    cursor.executemany("""
            INSERT INTO Contatos (ID,nome,Datanascimento,Telefone,Rua,NumeroResidencia,Complemento,Cidade,Estado,Pais,CEP)
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s);
        """, Contatos)
    
    conn.commit()

        # Fechamento da conexão
    cursor.close()
    conn.close()
    print("Tabela Aluno criada e populada com sucesso!")

def visualizar_contatos():
        try:
            conn= get_conexao_postgres("contatos", "postgres", "postgres")

            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Contatos;
            """)

            #Recuperação dos registros da tabela Aluno
            contatos = cursor.fetchall()

            #Exibição dos registros da tabela Aluno
            for i in contatos:
                print(i)
            
            # Fechamento da conexão
            cursor.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as erro:
            print(f"Erro ao buscar a tabela Aluno: {erro}")
        
# Leitura de Registros d)

def criar_consultas():
     conn= get_conexao_postgres("Contatos", "postgres", "postgres") #funcao fazendo conexao 
     cursor= conn.cursor() #conexando o cursor

     #mostre Todos os contatos na tabela.
     cursor.execute("SELECT * FROM Contatos;")
     contatos= cursor.fetchall()
     for i in contatos:
         print('\n')
         print(i)
     print('\n') 

    #mostre Contatos de uma cidade específica
     cursor.execute("SELECT nome,cidade FROM Contatos WHERE cidade='Curitiba'")    
     contatos_cidade= cursor.fetchall()
     for i,o in contatos_cidade:
          print(i,"mora em",o)
    
     cursor.execute("SELECT nome FROM Contatos WHERE Datanascimento < '01-01-1999'")
     pessoas=cursor.fetchall()
     for i in pessoas:
          print("Pessoas que nasceram antes do dia 01/01/199",i)
     print("Consultas feitas")
     cursor.close()
     conn.close()
            

def main(): #valor na funcao de conexao
    conn = get_conexao_postgres("contatos", "postgres", "postgres")
    #criar_tabela_contatos()
    #visualizar_contatos()
    #criar_consultas()
    

if __name__ == "__main__":
    main(); #chamando a main 