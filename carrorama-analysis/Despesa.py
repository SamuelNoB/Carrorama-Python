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
    def valor(self, val):
        if val =='':
            raise DescricaoEmBrancoException("Valor")

        val = float(val)
        if val <= 0:
            raise ValorInvalidoException("Valor")
        self._valor = val

    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    def __str__(self):
        return TipoDeDespesa(self.categoria).name + '\nValor: R$ ' + str(self.valor) + '\nData: ' + str(self.data) + "\n"
