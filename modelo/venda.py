
class Venda:
    def __init__(self,cliente,itens):
        self.cliente = cliente
        self.itens = itens

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.produto.valor * item.quantidade
            return total


class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade