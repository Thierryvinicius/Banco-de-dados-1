from controle.produtoC import ProdutoC
from modelo.conexao import Conexao
from modelo.cliente import Cliente
from controle.clienteC import ClienteC

# Configuração da conexão com o banco de dados

conexao = Conexao('localhost', 'teste', 'postgres', '3011')
cadastroC = ClienteC(conexao)
cadastroP = ProdutoC(conexao)
cadastroC.cadastrar_clientes()
cadastroP.cadastrar_produtos()
print(cadastroP.consultar_produtos())
print(cadastroC.consultar_clientes())
conexao.fechar_conexao()

