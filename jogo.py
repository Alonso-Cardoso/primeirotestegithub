
from random import random
import os

class Tabuleiro:
    def __init__(self):
        #Inicializa todas as posições com ' '
        self._posicoes = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
    def imprime(self):
        print('\n  | A | B |C',sep="")#impime as letras das colunas
        for cont, linha in enumerate(self._posicoes):
            
            print("_____________")
            print(cont+1, " | "+" | ".join(linha),sep='')
            
    def jogada(self,posicao,simbolo):
        try:
            linha = int(posicao[0]) - 1

            letra = posicao[1].upper()
            coluna = ord(letra) - ord('A')
            if self._posicoes[linha][coluna] == ' ':
                self._posicoes[linha][coluna] = simbolo
                return True

        except:
            pass
        return False
    
    def tem_jogada(self):
        for linha in self._posicoes:
            if ' ' in linha:
                return True
        
        return False
    
    def todas_as_linhas(self):
        todas = []

        for linha in self._posicoes:
            todas.append(tuple(linha))

        for cont in range(3):
            coluna = [self._posicoes[0][cont], self._posicoes[1][cont], self._posicoes[2][cont]]
            todas.append(tuple(coluna))

        diagonal = []
        tranversal = []
        for cont in range(3):
            diagonal.append(self._posicoes[cont][cont])
            tranversal.append(self._posicoes[2-cont][cont])

        todas.append(tuple(diagonal))
        todas.append(tuple(tranversal))
        return todas
    

class Velha:

    def __init__ (self):
        self._tabuleiro = Tabuleiro()

        if random() >= 0.5:
            self._jogador = 'X'
        else:
            self._jogador = 'O'

    def imprime(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('Jogo da Velha\n')
        self._tabuleiro.imprime()

    def troca_jogador(self):

        if self._jogador == 'X':
            self._jogador = 'O'
        else:
            self._jogador = 'X'

    def pega_jogada(self):

        while True:
            self.imprime()

            print('\n Jogador ', self._jogador)
            posicao = input('Digite a posição')
            print(posicao[0],posicao[1])

            input()

            if self._tabuleiro.jogada(posicao,self._jogador):
                break

    def eh_vencedor(self,jogador):
        linhas = self._tabuleiro.todas_as_linhas()

        if tuple([jogador]*3) in linhas:
            return True
        return False
    
    def jogar(self):

        while self._tabuleiro.tem_jogada():

            self.imprime()
            self.pega_jogada()

            if self.eh_vencedor(self._jogador):
                self.imprime()
                print('Fim de Jogo!')
                print('Vitória do jogador ',self._jogador)
                return
            self.troca_jogador()
        self.imprime()
        print('Jogo empatado!')


            




            
            
tab = Velha()
tab.jogar()
