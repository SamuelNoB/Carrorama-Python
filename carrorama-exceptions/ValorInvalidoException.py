class ValorInvalidoException(Exception):
    def __init__(self, NomeDoCampo):
        self.NomeDoCampo = NomeDoCampo

    def ToString(self):
        return "Valor invalido para o campo" + self.NomeDoCampo + "."