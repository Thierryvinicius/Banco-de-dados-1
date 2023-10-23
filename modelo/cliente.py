class Cliente:
    def __init__(self,nome,telefone,codigo):
        self.nome = nome
        self.telefone = telefone
        self.codigo = codigo

    def cadastrar_cliente(self):
        nome = input('Digite o nome do cliente: ')
        telefone = input('Digite o telefone do cliente: ')
        cod = input('Digite o codigo do cliente: ')

