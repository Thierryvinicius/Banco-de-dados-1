from modelo.conexao import Conexao
from modelo.cliente import Cliente
from modelo.produto import Produto

# Configuração da conexão com o banco de dados

conexao = Conexao('localhost', 'database', 'user', 'senha')
cadastroC = Cliente(conexao)
cadastroP = Produto(conexao)
cadastroC.cadastrar_clientes()
cadastroP.cadastrar_produtos()
print(cadastroP.consultar_produtos())
print(cadastroC.consultar_clientes())
conexao.fechar_conexao()

