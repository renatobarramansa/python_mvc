import pymssql

class ClientModel:
    def __init__(self, server, username, password, database):
        self.server = server
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pymssql.connect(
                server=self.server,
                user=self.username,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida!")
        except pymssql.Error as e:
            print(f"Erro ao conectar: {e}")
            self.connection = None
            self.cursor = None

    def create_database(self):
        try:
            # Conecta ao banco de dados 'master' para criar o novo banco de dados
            temp_connection = pymssql.connect(
                server=self.server,
                user=self.username,
                password=self.password,
                database='master'
            )
            temp_connection.autocommit(True)
            temp_cursor = temp_connection.cursor()
            
            create_db_query = f"""
            IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{self.database}')
            BEGIN
                CREATE DATABASE [{self.database}]
            END
            """
            temp_cursor.execute(create_db_query)
            print(f"Banco de dados '{self.database}' criado ou já existente.")
        except pymssql.Error as e:
            print(f"Erro ao criar o banco de dados: {e}")
        finally:
            if temp_cursor:
                temp_cursor.close()
            if temp_connection:
                temp_connection.close()

    def create_table(self):
        if self.cursor is None:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return
        create_table_query = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Clientes' AND xtype='U')
        CREATE TABLE Clientes (
            ID INT PRIMARY KEY,
            Nome NVARCHAR(100),
            Email NVARCHAR(100)
        )
        """
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Tabela 'Clientes' criada ou já existente.")
        except pymssql.Error as e:
            print(f"Erro ao criar a tabela: {e}")

    def insert_client(self, client_id, name, email):
        if self.cursor is None:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return
        insert_query = "INSERT INTO Clientes (ID, Nome, Email) VALUES (%d, %s, %s)"
        try:
            self.cursor.execute(insert_query, (client_id, name, email))
            self.connection.commit()
            print("Dados inseridos com sucesso.")
        except pymssql.Error as e:
            print(f"Erro ao inserir dados: {e}")
            self.connection.rollback()

    def delete_client(self,client_id):
        if self.cursor is None:
            print('Erro: Conexão com o banco de dados não estabelecida')
            return
        delete_query = 'DELETE FROM Clientes WHERE ID = %d'
        try:
            self.cursor.execute(delete_query, (client_id))
            self.connection.commit()
            print('Cliente excluído com sucesso.')
        except pymssql.Error as e:
            print(f"Erro ao ecluir cliente: {e}")
            self.connection.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão fechada.")
