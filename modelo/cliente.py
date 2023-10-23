class Cliente:
    def __init__(self,conexao,nome = '',telefone = '',codigo = ''):
        self.conexao = conexao
        self.nome = nome
        self.telefone = telefone
        self.codigo = codigo

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

    def getNome(self):
        return self.nome
    def getTelefone(self):
        return self.telefone
    def getCodigo(self):
        return self.codigo

