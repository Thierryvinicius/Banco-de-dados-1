class Cliente:
    def __init__(self,nome,telefone,codigo):
        self.nome = nome
        self.telefone = telefone
        self.codigo = codigo

    def getNome(self):
        return self.nome
    def getTelefone(self):
        return self.telefone
    def getCodigo(self):
        return self.codigo

