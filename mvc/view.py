class ClientView:
  @staticmethod
  def get_client_data():
    client_id = int(input("Digite o ID do cliente: "))
    name = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    return client_id, name, email
  
  def get_client_id(self):
    client_id = int(input("ID do cliente a ser excluído"))
    return client_id
