from Despesa import Despesa
from datetime import date
from ValorInvalidoException import ValorInvalidoException
from DescricaoEmBrancoException import DescricaoEmBrancoException


class Manutencao(Despesa):
    def __init__(self, quilometragem=0, data=date, valor=0.0):
        super().__init__(data, 3, valor)
        self._quilometragem = quilometragem

    @property
    def quilometragem(self):
        return self._quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):

        if valor == '':
            raise DescricaoEmBrancoException("Quilometragem")

        valor = int(valor)

        if valor < 0:
            raise ValorInvalidoException("Quilometragem")
        self._quilometragem = valor

    def __str__(self): return "Manutenção\nValor: R$" + str(self.valor) + "\nQuilometragem: " \
                              + str(self.quilometragem) + "\nData: " + str(self.data) + "\n"
