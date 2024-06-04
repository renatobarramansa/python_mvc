from model import ClientModel
''
def create_db():
    server = 'localhost'  # Por exemplo, 'localhost' ou '192.168.1.1'
    username = 'sa'
    password = 'Jogador@123'
    database = 'testes'

    model = ClientModel(server, username, password, database)
    model.create_database()

if __name__ == "__main__":
    create_db()
