class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.__nome = nome 
        self.__preco = preco 
        self.__quantidade_em_estoque = quantidade_em_estoque

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_preco(self):
        return self.__preco
    

    @get_preco.setter
    def preco(self, valor):
        if valor <= 0:
            self.__preco = valor
        else:
            print("Preco nao pode ser negativo")


    @property
    def get_quantidade_em_estoque(self):
        return self.__quantidade_em_estoque


    @get_quantidade_em_estoque.setter
    def quantidade_em_estoque(self, valor):
        if valor > 0:
            self.__quantidade_em_estoque = valor
        else:
            print("A quantidade em estoque nao pode ser negativa")


    def vender(self, quantidade):
        if quantidade < self.__quantidade_em_estoque:
            self.__quantidade_em_estoque -= quantidade
        else:
            print("Estoque insuficiente para venda")


    def repor_estoque(self, quantidade):
        self.__quantidade_em_estoque += quantidade
    

meu_produto = Produto("Notebook", 3500, 20)
print(f"Produto: {meu_produto.get_nome}, Preço: R${meu_produto.get_preco}, Estoque: {meu_produto.get_quantidade_em_estoque}")
meu_produto.vender(3)
meu_produto.repor_estoque(5)
meu_produto.vender(15)
print(f"Estoque atual: {meu_produto.get_quantidade_em_estoque}")