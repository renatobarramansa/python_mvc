from controller import ClientController

def main():
    # Defina as informações de conexão
    server = '127.0.0.1'  # Por exemplo, 'localhost' ou '192.168.1.1'
    username = 'sa'
    password = 'Jogador@123'
    # database = 'teste'

    # Crie uma instância do controlador e execute a aplicação
    controller = ClientController(server, username, password)
    controller.run()

if __name__ == "__main__":
    main()
