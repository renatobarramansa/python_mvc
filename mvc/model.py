import pymssql

class ClientModel:
  def __init__(self, server, username, password):
    self.server = server
    self.username = username
    self.password = password
    self.connection = None
    self.cursor = None
  
  def connect(self):
    try:
        self.connection = pymssql.connect(
          server = self.server,
          username = self.username,
          password = self.password
        )
        self.cursor = self.connection.cursor()
        print('Conexão bem sucedida !!!')
    except Exception as e:
       print(f'Erro ao conectar: {e}')

  
  def create_database(self):
        temp_connection = pymssql.connect(
            server=self.server,
            user=self.username,
            password=self.password,
            database='master'  # Conecta ao banco de dados 'master' para verificar/criar o novo banco
        )
        temp_cursor = temp_connection.cursor()
        
        create_db_query = f"""
        IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{self.database}')
        BEGIN
            CREATE DATABASE [{self.database}]
        END
        """
        try:
            temp_cursor.execute(create_db_query)
            temp_connection.commit()
            print(f"Banco de dados '{self.database}' criado ou já existente.")
        except Exception as e:
            print(f"Erro ao criar o banco de dados: {e}")
        finally:
            temp_cursor.close()
            temp_connection.close()

  
  
  
  
  def create_table(self):
        create_table_query = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Clientes' AND xtype='U')
        CREATE TABLE Clientes (
            ID INT PRIMARY KEY,
            Nome NVARCHAR(100),
            Email NVARCHAR(100)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

  def insert_client(self, client_id, name, email):
        insert_query = "INSERT INTO Clientes (ID, Nome, Email) VALUES (%d, %s, %s)"
        try:
            self.cursor.execute(insert_query, (client_id, name, email))
            self.connection.commit()
            print("Dados inseridos com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
            self.connection.rollback()

  def close(self):
        self.cursor.close()
        self.connection.close()
        print("Conexão fechada.")

    