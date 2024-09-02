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
        texto += ', Total: R${t:0.2f}'.format(t = self.total)
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
    
    def adiciona_produto(self,produto):
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
    
def pergunta(mensagem,tipo=int):
    while True:
        try:
            resp = input(mensagem)
            return tipo(resp)
        except:
            print('Valor Inválido!! Informe Novamente!')

def confirma(mensagem,resposta=str):
    texto = input(mensagem).lower().split()
    resp = resposta.lower()
    if resp in texto:
        return True
    return False

class Caixa:
    def __init__(self):
        self._produtos = {}
        self._vendas = []

    def menu(cls):
        print()
        print('********************************')
        print('* CAIXA *')
        print('********************************')
        print('(C) Cadastrar/atualizar produto ')
        print('(E) Entrada de estoque ')
        print('(V) Vender ')
        print('(R) Relatório de vendas ')
        print('(S) Sair ')
        print('********************************')
        escolha = input('Informe sua opção: ').upper()
        return escolha

    def busca_produto(self):
        if len(self._produtos) == 0:
            print('Nenhum produto cadastrado!!')
            return None
        for cod, produto in self._produtos.items():
            print(cod, ':',produto)
        codigo = pergunta('Código do produto:')
        if codigo in self._produtos:
            return self._produtos[codigo]
        print('Produto não encontrado!!')
        return None
    
    @classmethod
    def dados_produto(cls):
        print('Informe os dados: ')
        descricao = input('Descrição do produto: ')
        preco = pergunta('Preço',float)
        return descricao, preco
    
    def cadastro_produto(self):
        produto = self.busca_produto()
        if produto is not None:
            print('Produto Cadastrado: ', produto)
            if confirma('Alterar? (S/N)', 'S'):
                descricao, preco = self.dados_produto()
                produto.descricao = descricao
                produto.preco = preco

        else:
            if confirma('Incluir? (S/N)', 'S'):
                descricao, preco = self.dados_produto()
                produto = ProdutoEstoque(descricao, preco)
                codigo = len(self._produtos)
                self._produtos[codigo] = produto

    def entrada_estoque(self):
        produto = self.busca_produto()
        if produto is not None:
            quantidade = pergunta('Quantidade de entrada: ', float)
            produto.entrada(quantidade)

    def venda(self):
            print('Venda')
            venda = Venda()
            while True:
                produto = self.busca_produto()
                if produto is not None:
                    quantidade = pergunta('Quantidade vendida:', float)
                    if produto.saida(quantidade):
                        produto_venda = ProdutoVenda(produto.descricao,produto.preco,quantidade)
                        venda.adiciona_produto(produto_venda)
                print(venda)
                if confirma('Adicionar mais produtos: (S/N)', 'N'):
                    break
            if venda.numero_produtos > 0:
                self._vendas.append(venda)
    
    def relatorio_vendas(self):
        if len(self._vendas) == 0:
            print('Nenhuma venda efetuada')
            return
        total_geral = 0
        for cont, venda in enumerate(self._vendas):
            print('\nVenda ',cont)
            print(venda)
            total_geral += venda.total
            print('Total Geral: ', total_geral)            
            input('Pressione "ENTER" para voltar.')

    def iniciar(self):
        while True:
            escolha = self.menu()
            if escolha == 'C':
                self.cadastro_produto()
            elif escolha == 'E':
                self.entrada_estoque()
            elif escolha == 'V':
                self.venda()
            elif escolha == 'R':
                self.relatorio_vendas()
            elif escolha == 'S':
                break


if __name__ == '__main__':
    Caixa().iniciar()
 