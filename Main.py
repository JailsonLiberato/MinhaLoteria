#coding: utf-8
import random
import Constantes
from JTools import JToolsClass

class MainClass:
    
    jtools = JToolsClass()
    def __init__(self):
        self.jtools.clear()
        print("\n\n\n\t\t\t\t::::Minha Loteria::::")
        tipo_jogo = self.definirJogo()
        tipo_jogo = self.definirCaracteristicasJogo(tipo_jogo)
        numeros = self.gerarValoresRandom(tipo_jogo)
        self.imprimir(numeros)

    def definirJogo(self):
        while True:
            print("\n\n\t[Menu de jogos]")
            print("[1] Mega Sena")
            print("[2] Lotofácil")
            print("[3] Lotomania")
            print("[4] Dupla Sena")
            print("[5] Quina")
            quantidade = raw_input("\nESCOLHA OPÇÃO: ")
            if quantidade.isdigit() and (int(quantidade) >= 1 and int(quantidade) <= 5):
                return quantidade 
    
    def definirCaracteristicasJogo(self, tipo_jogo):
        switcher = {
            "1": Constantes.MEGA_SENA,
            "2": Constantes.LOTOFACIL,
            "3": Constantes.LOTOMANIA,
            "4": Constantes.DUPLA_SENA,
            "5": Constantes.QUINA
        }
        return switcher[tipo_jogo]

    def gerarValoresRandom(self, tipo_jogo):
        numeros = []
        i = 0
        while i < tipo_jogo[0]:
            numero = random.randint(tipo_jogo[1],tipo_jogo[2])
            if not numero in numeros:
                numeros.append(numero)
                i = i + 1 
        return numeros

    def imprimir(self, numeros):
        print("\n")
        numeros.sort()
        for numero in numeros:
            print(numero),
        print("\n")


main = MainClass()