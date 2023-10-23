class ClienteC:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_clientes(self):
        cursor = self.conexao._db.cursor()
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        codigo = int(input('Digite o código: '))
        cursor.execute(f"INSERT INTO cliente VALUES ('{nome}','{telefone}','{codigo}')")
        self.conexao._db.commit()



    def consultar_clientes(self):
        cursor = self.conexao._db.cursor()
        cursor.execute('SELECT * FROM cliente')
        resultados = cursor.fetchall()
        cursor.close()
        return resultados


