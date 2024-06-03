from model import ClientModel
from view import ClientView

class ClientController:
    def __init__(self, server, username, password):
        self.model = ClientModel(server, username, password)
        self.view = ClientView()

    def run(self):
        # Cria o banco de dados se ele não existir
        # self.model.create_database()
        # Conecta ao banco de dados
        self.model.connect()
        # Verifica se a conexão foi bem-sucedida antes de prosseguir
        if self.model.connection and self.model.cursor:
            # Cria a tabela 'Clientes' se ela não existir
            self.model.create_table()
            
            # Obtém dados do cliente da visão (entrada do usuário)
            client_id, name, email = self.view.get_client_data()
            # Insere os dados do cliente no banco de dados usando o modelo
            self.model.insert_client(client_id, name, email)
            
            # Fecha a conexão com o banco de dados
            self.model.close()
        else:
            print("Erro: Conexão com o banco de dados não foi estabelecida.")
