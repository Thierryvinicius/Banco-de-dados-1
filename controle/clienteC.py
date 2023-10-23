class ClienteC:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_clientes(self,nome,telefone,codigo):
        cursor = self.conexao._db.cursor()
        cursor.execute(f"INSERT INTO cliente VALUES ('{nome}','{telefone}','{codigo}')")



    def consultar_clientes(self):
        cursor = self.conexao._db.cursor()
        cursor.execute('SELECT * FROM cliente')
        resultados = cursor.fetchall()
        cursor.close()
        return resultados


