from Despesa import Despesa

class Manutencao(Despesa):
    def __init__(self, quilometragem=0):
        super().__init__()
        self.quilometragem = quilometragem


    @property
    def quilometragem(self):
        return self.quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        self.quilometragem = valor
