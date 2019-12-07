from datetime import date
from TipoDeDespesa import TipoDeDespesa
from DescricaoEmBrancoException import DescricaoEmBrancoException
from ValorInvalidoException import ValorInvalidoException


class Despesa:
    def __init__(self, data=date, categoria=TipoDeDespesa, valor=0.0):
        self.data = data.today()
        self._categoria = categoria
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @property
    def categoria(self):
        return self._categoria

    @valor.setter
    def valor(self, valor):
        if valor is "":
            raise DescricaoEmBrancoException("Valor da despesa")
        valor = float(valor)
        if valor <= 0:
            raise ValorInvalidoException("Valor da Despesa")
        self._valor = valor

    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    def __str__(self):
        return self.categoria.name + '\nValor: R$ ' + str(self.valor) + '\nData: ' + str(self.data) + "\n\n"
