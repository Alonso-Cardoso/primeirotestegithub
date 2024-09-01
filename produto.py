class Produto:
    
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco
        
    def __str__(self):
        return '{d} (R${p:0.2f})'.format(d=self._descricao,p=self._preco)     

class ProdutoEstoque(Produto):
    def __init__(self,descricao,preco):
        super().__init__(descricao,preco)
        self._estoque = 0.0

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,preco):
        self._preco = preco

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self,descricao):
        self._descricao = descricao

    def entrada(self,quantidade):
        self._estoque += quantidade

    def saida(self,quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False
    
    
    def __str__(self):
        texto = super().__str__()
        texto += ', Estoque: {e:0.2f}'.format(e = self._estoque)
        return texto
class ProdutoVenda(Produto):
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self._quantidade = quantidade

    @property
    def total(self):
        return self._quantidade * self._preco
    
    def __str__(self):
        texto = super().__str__()
        texto += ', Quantidade: {q:0.3f}'.format(q = self._quantidade)
        texto += ', Total: R${t:0.2f}'.format(t = self.total())
        return texto

class Venda:
    def __init__(self):
        self._produtos = []
        self._total = 0.0

    @property
    def total(self):
        return self._total
    
    @property
    def numero_produtos(self):
        return len(self._produtos)
    
    def adicona_produto(self,produto):
        self._produtos.append(produto)
        self._total += produto.total

    def __str__(self):
        texto = '\n' + '-'*50
        texto += '\nProdutos: '
        for produto in self._produtos:
            texto += '\n' + str(produto)
        texto += '\n' + '-'*50
        texto += 'Total da venda: {t:0.2f}'.format(t=self._total)
        texto += '\n' + '-'*50
        return texto
        


prod = ProdutoEstoque('Arroz',12.5)
print (prod.__str__())
