import psycopg2


class Conexao:
    def __init__(self, mhost, db, usr, pwd):
        try:
            self._db = psycopg2.connect(host=mhost, database=db, user=usr, password=pwd)
            self.cur = self._db.cursor()
            print('Conectado ao Postgres!')
        except:
            print('Falha na conexão com o Postgres!')

    def fechar_conexao(self):
        self._db.close()
