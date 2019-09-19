from datetime import date
from TipoDeDespesa import TipoDeDespesa

class Despesa:
    def __init__(self, nome="", data=date, categoria = TipoDeDespesa, valor=0.0):
        self.nome = nome
        self.data = data
        self.categoria = categoria
        self.valor = valor

    @property
    def nome(self):
        return self.nome
    @property
    def valor(self):
        return self.valor

    @nome.setter
    def nome(self, valor):
        self.nome = valor

    @valor.setter
    def valor(self, valor):
        self.valor = valor
