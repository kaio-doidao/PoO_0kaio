class ItemPedido:
    def __init__(self, produto, quantidade, preço):
        self.produto = produto
        self.quantidade = quantidade
        self.preço = preço

    def __str__(self):
        return f"Nome do produto: {self.produto} - Quantidade: {self.quantidade} - Preço: R${self.preço}"
    
class Pedido:
    def __init__(self):
        self.lista_de_itens = []
    
    def adicionar_item(self, produtos):
        self.lista_de_itens.append(produtos)

    def calcular_total(self):
        soma_total = 0
        for produto in self.lista_de_itens:
            soma_total += produto.preço
        print(f"Soma total dos produtos = R${soma_total}")
    
    def listar_itens(self):
        for produtos in self.lista_de_itens:
            print(produtos)

item1 = ItemPedido("Celular", 2000, 1300.00)
item2 = ItemPedido("Tablet", 200, 2500.00)
pedido = Pedido()
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)
pedido.listar_itens()
pedido.calcular_total()