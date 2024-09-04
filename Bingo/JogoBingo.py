from random import shuffle
from os import system, name
class Jogador:
    
    def __init__(self, nome):
        self._nome = nome
        linhaB = []
        linhaI = []
        linhaN = []
        linhaG = []
        linhaO = []

        for b in range (1,21):
            linhaB.append(b)
        shuffle(linhaB)
        #print(linhaB)
        for i in range (21,41):
            linhaI.append(i)
        shuffle(linhaI)
        for n in range (41,61):
            linhaN.append(n)
        shuffle(linhaN)

        for g in range (61,81):
            linhaG.append(g)
        shuffle(linhaG)
        for o in range (81,101):
            linhaO.append(o)    
        shuffle(linhaO)
          
        self._cartela = [[],[],[],[],[]]
        for cont,linha in enumerate(self._cartela):
            if cont == 0:
                for cont2 in range(5):
                    bola = linhaB.pop()
                    linha.append(bola)
                linha.sort()
            elif cont == 1:
                for cont2 in range(5):
                    bola = linhaI.pop()
                    linha.append(bola)
                linha.sort()
            elif cont == 2:
                for cont2 in range(5):
                    bola = linhaN.pop()
                    linha.append(bola)
                linha.sort()
            elif cont == 3:
                for cont2 in range(5):
                    bola = linhaG.pop()
                    linha.append(bola)
                linha.sort()
            elif cont == 4:
                for cont2 in range(5):
                    bola = linhaO.pop()
                    linha.append(bola)
                linha.sort()
                
        #print(self._cartela)
    @property
    def nome(self):
        return self._nome
        
    def imprime(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear')    
        i = 0
        
        print('****Cartela****')
        print('|B |I |N |G |O |',sep='')
        print('_________________')
        for cont in range(len(self._cartela)):
            print('|',end='')
            for cont2 in range(len(self._cartela[cont])):
                print('{d:2}|'.format(d=self._cartela[cont2][cont]),sep='',end='',)
                
            print()              
             #   print('|{d}|'.format(d=cont2))
                
            #d  = linha[i]
            
       


class Bingo():
    
    def __init__(self):
        self._sorteio = []
        for cont in range(1,101):
            self._sorteio.append(cont)
        shuffle(self._sorteio)
        
    def numeros_sorteio(self):
        return self._sorteio
        
        
jogo = Jogador('kaka')
jogo.imprime()
        
#print(Bingo().numeros_sorteio()) 