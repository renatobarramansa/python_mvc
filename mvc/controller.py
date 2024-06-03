from model import ClientModel
from view import ClientView

class ClientController:
    def __init__(self, server, username, password, database):
        # Inicializa o modelo e a visão
        self.model = ClientModel(server, username, password, database)
        self.view = ClientView()

    def run(self):
        # Conecta ao banco de dados
        self.model.connect()
        # Cria a tabela 'Clientes' se ela não existir
        self.model.create_table()
        
        # Obtém dados do cliente da visão (entrada do usuário)
        client_id, name, email = self.view.get_client_data()
        # Insere os dados do cliente no banco de dados usando o modelo
        self.model.insert_client(client_id, name, email)
        
        # Fecha a conexão com o banco de dados
        self.model.close()
