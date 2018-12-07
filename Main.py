#coding: utf-8
import random
from JTools import JToolsClass

class MainClass:
    
    jtools = JToolsClass()
    def __init__(self):
        self.jtools.clear()
        print("\n\n\n\t\t\t\t::::Minha Loteria::::")
        quantidade = self.definirQuantidadeNumeros()
        numeros = self.gerarValoresRandom(quantidade)
        self.imprimir(numeros)
    
    def definirQuantidadeNumeros(self):
        while True:
            quantidade = input("\nDigite quantidade de números: ")
            if type(quantidade) == int:
                return quantidade

    def gerarValoresRandom(self, quantidade):
        numeros = []
        i = 0
        while i < quantidade:
            numero = random.randint(1,25)
            if not numero in numeros:
                numeros.append(numero)
                i = i + 1 
        return numeros

    def imprimir(self, numeros):
        for numero in numeros:
            print(numero)



main = MainClass()