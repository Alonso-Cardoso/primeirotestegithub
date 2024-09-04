from random import shuffle
class Jogador:
    
    def __init__(self, nome):
        self._nome = nome
        self._cartela = [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
        
    @property
    def nome(self):
        return self._nome
        
class Bingo():
    
    def __init__(self):
        self._sorteio = []
        for cont in range(1,101):
            self._sorteio.append(cont)
        shuffle(self._sorteio)
        
    def numeros_sorteio(self):
        return self._sorteio
        
        
jogo = Jogador('kaka')
        
#print(Bingo().numeros_sorteio()) 