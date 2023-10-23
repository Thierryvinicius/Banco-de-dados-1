from modelo.conexao import Conexao
from modelo.cliente import Cliente
from controle.clienteC import ClienteC

# Configuração da conexão com o banco de dados

conexao = Conexao('localhost', 'database', 'usuario', 'senha')
cadastro = ClienteC(conexao)
cadastro.cadastrar_clientes('usuario','numero','1')
print(cadastro.consultar_clientes())
conexao.fechar_conexao()

