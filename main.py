from modelo.conexao import Conexao
from modelo.cliente import Cliente
from controle.clienteC import ClienteC

# Configuração da conexão com o banco de dados

conexao = Conexao('localhost', 'teste', 'postgres', '3011')
cadastro = ClienteC(conexao)
cadastro.cadastrar_clientes()
print(cadastro.consultar_clientes())
conexao.fechar_conexao()

