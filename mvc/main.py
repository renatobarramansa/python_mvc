from controller import ClientController
import os
from dotenv import load_dotenv

def main():
    # Defina as informações de conexão
    load_dotenv()
    
    server = os.getenv('DB_SERVER')
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    # Crie uma instância do controlador e execute a aplicação
    controller = ClientController(server, username, password,database)
    controller.run()

if __name__ == "__main__":
    main()
