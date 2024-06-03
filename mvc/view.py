class ClientView:
  @staticmethod
  def get_client_data():
    client_id = int(input("Digite o ID do cliente: "))
    name = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    return client_id, name, email
  
  @staticmethod
  def display_message(message):
    print(message)
