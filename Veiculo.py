import re
from DescricaoEmBrancoException import DescricaoEmBrancoException
from ValorInvalidoException import ValorInvalidoException
from Combustivel import Combustiveis
from Despesa import Despesa


class Veiculo:

    def __init__(self, marca="", modelo="", ano=0, motor=0.0, combustiveis=(), cor="", placa="", renavam=""):
        try:
            self._marca = marca
            self._modelo = modelo
            self._ano = ano
            self._motor = motor
            self._combustiveis = combustiveis
            self._cor = cor
            self._placa = placa
            self._renavam = renavam
            self.despesas = []
        except(DescricaoEmBrancoException or ValorInvalidoException) as e:
            raise e

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    @property
    def motor(self):
        return self._motor

    @property
    def combustiveis(self):
        return self._combustiveis

    @property
    def cor(self):
        return self._cor

    @property
    def placa(self):
        return self._placa

    @property
    def renavam(self):
        return self._renavam

    @marca.setter
    def marca(self, valor):
        if valor is None:
            DescricaoEmBrancoException("Marca")
        else:
            self._marca = valor

    @modelo.setter
    def modelo(self, valor):
        if valor is None:
            raise DescricaoEmBrancoException("Nome")

        self._modelo = valor

    @ano.setter
    def ano(self, valor):
        if valor < 1900:
            raise ValorInvalidoException("Ano")
        self._ano = valor

    @motor.setter
    def motor(self, valor):
        if valor < 0:
            raise ValorInvalidoException("Motor")
        self._motor = valor

    @placa.setter
    def placa(self, valor):
        if not re.match(r'([A-z]{3}-[0-9]{4})', valor):
            raise ValorInvalidoException("Placa")
        else:
            self._placa = valor.upper()

    @cor.setter
    def cor(self, valor):
        if valor is None:
            raise DescricaoEmBrancoException("Cor")
        self._cor = valor

    @renavam.setter
    def renavam(self, valor):
        somadigitos = 0
        multiplicador = 3
        if not re.match(r'([0-9]{4}[.][0-9]{6}-[0-9])', valor):
            print("nao combinou")
            raise ValorInvalidoException("Renavam")
        else:
            print("combinou")
            for i in range(len(valor)-1):

                somadigitos += (int(valor[i]) * multiplicador)
                if multiplicador == 2:
                    multiplicador = 10
                multiplicador -= 1
            somadigitos = (somadigitos * 10) % 11
            if somadigitos == 10:
                somadigitos = 0
            if somadigitos == int(valor[10]):
                self._renavam = valor
            else:
                raise ValorInvalidoException("Renavam")

    @combustiveis.setter
    def combustiveis(self, valor):
        if valor[0] is None and valor[1] is None:
            raise DescricaoEmBrancoException("Combustíveis")
        if valor[0] is not None and valor[1] is None:
            self._combustiveis = (valor[0])
        elif valor[0] is not None and valor[1] is not None:
            self._combustiveis = (valor[0], valor[1])

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' ' + self.cor + ' ' + str(self.ano) + ' - ' + self.placa
