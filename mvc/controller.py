from model import ClientModel
from view import ClientView

class ClientController:
    def __init__(self, server, username, password,database):
        self.model = ClientModel(server, username, password,database)
        self.view = ClientView()

    def run(self):        
        self.model.connect()        
        if self.model.connection and self.model.cursor:            
            self.model.create_table()
            
            while True:
                print("1. Inserir novo cliente")
                print("2. Excluir cliente")
                print("3. Sair")
                choice = input("Escolha uma opção: ")
                
                if choice == '1':
                    client_id, name, email = self.view.get_client_data()
                    self.model.insert_client(client_id, name, email)
                elif choice == '2':
                    client_id = self.view.get_client_id()
                    self.model.delete_client(client_id)
                elif choice == '3':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            
            self.model.close()
        else:
            print("Erro: Conexão com o banco de dados não foi estabelecida.")
