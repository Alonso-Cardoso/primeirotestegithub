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



prod = ProdutoEstoque('Arroz',12.5)
print (prod.__str__())
