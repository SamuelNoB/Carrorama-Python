from datetime import date
from TipoDeDespesa import TipoDeDespesa
from DescricaoEmBrancoException import DescricaoEmBrancoException
from ValorInvalidoException import ValorInvalidoException


class Despesa:
    def __init__(self, nome="", data=date, categoria=TipoDeDespesa, valor=0.0):
        self.data = data
        self._categoria = categoria
        try:
            self._nome = nome
            self._valor = valor
        except (DescricaoEmBrancoException or ValorInvalidoException) as e:
            raise e

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @nome.setter
    def nome(self, valor):
        if valor is None:
            raise DescricaoEmBrancoException("Nome")
        self._nome = valor

    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValorInvalidoException("Valor da Despesa")
        self._valor = valor
