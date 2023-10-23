

class ProdutoC:

    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrar_produtos(self):
        cursor = self.conexao._db.cursor()
        nomeP = input('Digite o nome do produto: ')
        codigo = input('Digite o código do produto: ')
        preco = float(input('Digite o preço do produto: '))
        qtd = int(input('Digite a quantidade do produto: '))
        cursor.execute(f"INSERT INTO produtos VALUES ('{nomeP}','{codigo}','{preco}','{qtd}')")
        self.conexao._db.commit()


    def consultar_produtos(self):
        cursor = self.conexao._db.cursor()
        cursor.execute('SELECT * FROM produtos')
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
