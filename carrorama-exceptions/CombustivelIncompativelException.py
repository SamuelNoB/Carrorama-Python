from Combustivel import Combustiveis
from Veiculo import Veiculo


class CombustivelIncompativel(Exception):
    def __init__(self, combustivel=Combustiveis, veiculo=Veiculo()):
        self.combustivel = combustivel.value
        self.veiculo = veiculo

    def __str__(self):
        return ("O combustivel" + self.combustivel + "é incompativel com o veiculo" + self.veiculo.marca + " " +
                self.veiculo.modelo + ".")
