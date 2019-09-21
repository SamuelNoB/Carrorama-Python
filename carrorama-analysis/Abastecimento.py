from .Despesa import Despesa
from datetime import date
from .TipoDeDespesa import TipoDeDespesa
from ..Combustivel import Combustiveis

class Abastecimento(Despesa):
    def __init__(self, combustivel = Combustiveis, QuilometragemInicial=0, ValorDoLitro=0.0, IsTanqueCheio=bool, nome="", data=date, valor=0.0):
        super().__init__(nome, data, TipoDeDespesa.Abastecimento, valor)
        self.combustivel = combustivel.name
        self.QuilometragemInicial = QuilometragemInicial
        self.ValorDoLitro = ValorDoLitro
        self. IsTanqueCheio = IsTanqueCheio


    @property
    def QuilometragemInicial(self):
        return self.QuilometragemInicial

    @QuilometragemInicial.setter
    def QuilometragemInicial(self, valor):
        self.QuilometragemInicial = valor

    @property
    def ValorDoLitro(self):
        return self.ValorDoLitro

    @ValorDoLitro.setter
    def ValorDoLitro(self, valor):
        self.ValorDoLitro = valor

    @property
    def Combustivel(self):
        return  self.Combustivel

    @Combustivel.setter
    def Combustivel(self, valor):
        self.Combustivel = valor