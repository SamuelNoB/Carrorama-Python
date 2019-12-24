from ValorInvalidoException import ValorInvalidoException
from DescricaoEmBrancoException import DescricaoEmBrancoException
from Despesa import Despesa
from datetime import date
from TipoDeDespesa import TipoDeDespesa
from Combustivel import Combustiveis


class Abastecimento(Despesa):

    def __init__(self, combustivel=None, QuilometragemInicial=0, ValorDoLitro=0.0, IsTanqueCheio=0,data=date, valor=0.0):
        super().__init__(data.today(), TipoDeDespesa.Abastecimento, valor)
        self._combustivel = combustivel
        self._QuilometragemInicial = QuilometragemInicial
        self._ValorDoLitro = ValorDoLitro
        self._IsTanqueCheio = IsTanqueCheio


    @property
    def QuilometragemInicial(self):
        return self._QuilometragemInicial

    @property
    def IsTanqueCheio(self):
        return self._IsTanqueCheio

    @IsTanqueCheio.setter
    def IsTanqueCheio(self, valor):
        self._IsTanqueCheio = int(valor)

    @QuilometragemInicial.setter
    def QuilometragemInicial(self, valor):
        if valor == '':
            raise DescricaoEmBrancoException("Quilometragem")

        valor = int(valor)
        if valor >= 0:
            self._QuilometragemInicial = valor
        else:
            raise ValorInvalidoException("Quilometragem")

    @property
    def ValorDoLitro(self):
        return self._ValorDoLitro

    @ValorDoLitro.setter
    def ValorDoLitro(self, valor):
        if valor == '':
            raise DescricaoEmBrancoException("Valor do litro")

        valor = float(valor)

        if valor < 0.0:
            raise ValorInvalidoException("Valor do litro")

        self._ValorDoLitro = valor

    @property
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, valor):
        self._combustivel = valor

    def __str__(self): return "\nAbastecimento.\nValor: R$" + str(self.valor) + "\nCombustivel usado: " + Combustiveis(self.combustivel).name + \
                              "\nValor do litro: R$ " + str(self.ValorDoLitro) + "\nQuilometragem:" + str(self.QuilometragemInicial) + "\nData: " + \
                              str(self.data) + "\n"
