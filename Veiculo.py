import sys
#sys.path.append("./Combustivel")

class Veiculo():
    def __init__(self, marca="", modelo="", ano=0, motor=0.0, combustiveis =[],cor="",placa="",renavan=""):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._motor = motor
        self._combustiveis = combustiveis
        self._cor = cor
        self._placa = placa
        self._renavan = renavan


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

    @property  # implementar a validação de placa
    def placa(self):
        return self._placa

    @property  # implementar a validação de renavan
    def renavan(self):
        return self._renavan

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @ano.setter
    def ano(self, valor):
        self._ano = valor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @placa.setter
    def placa(self, valor):
        self._placa = valor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @renavan.setter
    def renavan(self, valor):
        self._renavan = valor

    @combustiveis.setter
    def combustiveis(self, combustivel1):
        self._combustiveis.append(combustivel1.name)
