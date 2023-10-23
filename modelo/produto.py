class Produto:
    def __init__(self,conexao, nome = '',codigo = '',preco = 0.0,qtd = 0):
        self.conexao = conexao
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.qtd = qtd

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